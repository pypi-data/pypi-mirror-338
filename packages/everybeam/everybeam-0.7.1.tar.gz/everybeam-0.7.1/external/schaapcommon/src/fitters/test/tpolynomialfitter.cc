// Copyright (C) 2022 ASTRON (Netherlands Institute for Radio Astronomy)
// SPDX-License-Identifier: GPL-3.0-or-later

#include "polynomialfitter.h"

#include <boost/test/unit_test.hpp>
#include <boost/test/tools/floating_point_comparison.hpp>

using schaapcommon::fitters::PolynomialFitter;

BOOST_AUTO_TEST_SUITE(polynomial_fitter)

BOOST_AUTO_TEST_CASE(fit) {
  PolynomialFitter fitter;
  std::vector<float> terms;
  fitter.AddDataPoint(0.0, 0.0, 1.0);
  fitter.AddDataPoint(1.0, 0.0, 1.0);
  fitter.AddDataPoint(2.0, 1.0, 1.0);
  fitter.AddDataPoint(3.0, 2.0, 1.0);
  fitter.Fit(terms, 2);

  BOOST_CHECK_CLOSE_FRACTION(terms[0], -0.3, 1.0e-3);
  BOOST_CHECK_CLOSE_FRACTION(terms[1], 0.7, 1.0e-3);
}

BOOST_AUTO_TEST_CASE(fit_weighted) {
  PolynomialFitter fitter;
  std::vector<float> terms;
  fitter.AddDataPoint(0.0, 0.0, 1.5);
  fitter.AddDataPoint(1.0, 0.0, 1.5);
  fitter.AddDataPoint(2.0, 1.0, 0.5);
  fitter.AddDataPoint(3.0, 1.0, 0.5);
  fitter.Fit(terms, 1);

  BOOST_CHECK_CLOSE_FRACTION(terms[0], 0.25, 1.0e-3);
}

BOOST_AUTO_TEST_CASE(evaluate) {
  PolynomialFitter fitter;
  std::vector<float> terms;
  terms.push_back(-0.3);
  terms.push_back(0.7);

  BOOST_CHECK_CLOSE_FRACTION(PolynomialFitter::Evaluate(0.0, terms), -0.3,
                             1.0e-3);
  BOOST_CHECK_CLOSE_FRACTION(PolynomialFitter::Evaluate(1.0, terms), 0.4,
                             1.0e-3);
  BOOST_CHECK_CLOSE_FRACTION(PolynomialFitter::Evaluate(2.0, terms), 1.1,
                             1.0e-3);
  BOOST_CHECK_CLOSE_FRACTION(PolynomialFitter::Evaluate(3.0, terms), 1.8,
                             1.0e-3);
}

BOOST_AUTO_TEST_SUITE_END()
