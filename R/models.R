# Generative process models of anchored estimation on the log scale.
# All quantities are log(value / true value); sigma is the item's belief uncertainty,
# and every model parameter is expressed in units of sigma, so the models are scale-free.
#
# Each participant-item row has a belief centre mu = bias + person offset + belief noise.
# Response = model output + response noise; a small share of responses is contaminated
# (unit errors, typing slips) to mimic real estimation data.

belief_sd_share <- 0.6     # SD of belief centres across people, in sigma units
response_sd_share <- 0.3   # response noise SD, in sigma units
contamination_p <- 0.02    # share of responses with gross errors
contamination_sd <- 2      # SD (log units) of gross errors

model_names <- c(M0 = "No anchoring", M1 = "Anchor-and-adjust, fixed number of adjustments",
                 M1R = "Resource-rational anchor-and-adjust (adaptive number of adjustments)",
                 M2 = "Constant-weight integration", M3 = "Adjust to plausible boundary",
                 M4 = "Plausibility-discounted integration")

# Metropolis-Hastings adjustment from the anchor towards the belief N(mu, sigma^2)
# (Lieder et al., 2018a). steps can differ by row; proposals have SD s * sigma.
adjust <- function(x, mu, sigma, s, steps) {
  z <- x
  for (i in seq_len(max(steps))) {
    active <- steps >= i
    prop <- z + rnorm(length(z), 0, s * sigma)
    log_ratio <- ((z - mu)^2 - (prop - mu)^2) / (2 * sigma^2)
    z <- ifelse(active & log(runif(length(z))) < log_ratio, prop, z)
  }
  z
}

# Resource-rational number of adjustments: t* minimises the expected absolute error under the
# agent's own belief plus a time cost c per adjustment (Lieder et al., 2018a, Eq. 2). The expected
# error after t steps from a standardised start distance z is tabulated once per step size s.
rr_z_grid <- seq(0, 12, by = 0.1)
rr_max_t <- 300
rr_error_curves <- local({
  cache <- list()
  function(s) {
    key <- as.character(s)
    if (is.null(cache[[key]])) {
      n <- 3000
      err <- matrix(NA_real_, length(rr_z_grid), rr_max_t + 1)
      abs_err <- function(y) 2 * dnorm(y) + y * (2 * pnorm(y) - 1)   # E|y - X|, X ~ N(0, 1)
      # Fixed seed that restores the caller's random-number state afterwards
      withr::with_seed(424242, for (j in seq_along(rr_z_grid)) {
        z <- rep(rr_z_grid[j], n)
        err[j, 1] <- mean(abs_err(z))
        for (t in seq_len(rr_max_t)) {
          prop <- z + rnorm(n, 0, s)
          z <- ifelse(log(runif(n)) < (z^2 - prop^2) / 2, prop, z)
          err[j, t + 1] <- mean(abs_err(z))
        }
      })
      cache[[key]] <<- err
    }
    cache[[key]]
  }
})
rr_steps <- function(dist_sd, s, cost) {
  err <- rr_error_curves(s)
  t_star <- apply(err, 1, function(e) which.min(e + cost * (seq_along(e) - 1)) - 1)
  t_star[pmin(round(dist_sd / 0.1) + 1, length(rr_z_grid))]
}

respond <- function(model, x, mu, sigma, par) {
  d <- x - mu
  switch(model,
    M0 = mu,
    M2 = mu + par$w * d,
    M3 = ifelse(abs(d) < par$k * sigma, x, mu + sign(d) * par$k * sigma),
    M4 = mu + par$w * d * exp(-d^2 / (2 * (par$c * sigma)^2)),
    M1 = adjust(x, mu, sigma, par$s, rep(par$t, length(x))),
    M1R = {
      # kappa: the agent's own uncertainty relative to the spread of beliefs across people
      sig <- par$kappa * sigma
      adjust(x, mu, sig, par$s, rr_steps(abs(d) / sig, par$s, par$cost))
    })
}

# rows: data.table with x (log anchor / truth), cell, pid. cellpar: data.table with cell, bias, sigma.
simulate_responses <- function(model, rows, cellpar, par, person_sd = 0.15) {
  r <- merge(rows[, .(row_id = .I, cell, pid, x)], cellpar, by = "cell")
  setorder(r, row_id)
  persons <- unique(r$pid)
  u <- setNames(rnorm(length(persons), 0, person_sd), persons)
  mu <- r$bias + u[r$pid] + rnorm(nrow(r), 0, belief_sd_share * r$sigma)
  y <- respond(model, r$x, mu, r$sigma, par) + rnorm(nrow(r), 0, response_sd_share * r$sigma)
  gross <- runif(nrow(r)) < contamination_p
  y[gross] <- y[gross] + rnorm(sum(gross), 0, contamination_sd)
  y
}

# Anchoring index of each model in the Jacowitz & Kahneman (1995) design: anchors at the
# 15th and 85th percentiles of the unanchored response distribution.
jk_index <- function(model, par, n = 20000) {
  sd_unanchored <- sqrt(belief_sd_share^2 + response_sd_share^2)
  a <- qnorm(0.85) * sd_unanchored
  y_of <- function(x) {
    mu <- rnorm(n, 0, belief_sd_share)
    respond(model, rep(x, n), mu, 1, par) + rnorm(n, 0, response_sd_share)
  }
  (median(y_of(a)) - median(y_of(-a))) / (2 * a)
}
