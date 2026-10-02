# Calculation verification — 2026-10-02

## Scope and result
41 selected scenarios, 533 scalar comparisons passed (relative tolerance 1e-8; maximum observed relative error 4.60e-14). Additional 34 boundary, scaling and invalid-input assertions passed. This validates selected formulas and model implementation, not complete scaffold safety or universal code compliance.

Cases: terrain A/B/C × gust fixed/rigid/flexible/manual × wind auto/manual/net (36), plus 5 heights. Python independently evaluates tube properties, ASD compression, wind speed pressure and gust equations. Bracket redundant reaction is independently solved by numerical integration of dU/dVB = 0, splitting the horizontal beam at both point loads, using equal EI and neglecting axial deformation. Vertical reaction sum and moment equilibrium, anchor individual capacities and column utilization are checked.

Boundary checks: table 2.11 phi divisions, solid-sign interpolation, minimum z=5m wind pressure, velocity-squared and tributary-area scaling, invalid inputs, continuity at Cc, optional bracket and custom section.

## Official sources reviewed
- https://www.nlma.gov.tw/ch/legislation/regsearch/166
- https://www.nlma.gov.tw/uploads/files/ed1498837647323cbd8cd287ce939972.pdf (Chapter 2, sections 2.2, 2.6, 2.7)
- https://www.nlma.gov.tw/uploads/files/31dfde31df0c1be76c1b8d92e4285d76.pdf (tables 2.2, 2.10, 2.11)
- https://www.ilosh.gov.tw/90734/90811/136446/90775/91611/?cprint=pt

The official listed wind code remains the 104 implementation version including 103-12-03 corrections; research projects are not treated as effective amendments.

## Engineering limitations
ASD column and linear angle-member interaction retain the source program's model. No complete check of second-order effects, lateral-torsional buckling, overall stability, foundations or anchor concrete/group failures. Wind coefficient tables for independent signs/lattice are engineering analogies for attached scaffolds, not a certification. Netting and building interference need project-specific evidence. Phi 0.29–0.30 extends the preceding bin; flat-member coefficient is conservative in that gap. Top wind pressure envelopes tie tributary loads; whole-structure torsion from oblique wind is not checked.

## UI validation
Desktop live GitHub page rendered correctly. Input changed V=42.5 to 50 m/s: tie force changed 1397.68 to 1934.51 kgf (velocity-squared relation), restored afterward. Word generation shows exported status; remote browser download event could not be captured. The underlying bundled DOCX generation was previously tested. Responsive CSS provides single-column phone forms, 44–48px targets and fixed bottom workspace switching. No physical-phone/device-emulation visual test was completed in this environment.
