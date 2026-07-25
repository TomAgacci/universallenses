License Public Domain
# Universal Meta‑Lens System (UMLS)
A parallax‑adaptive, fully universal corrective lens architecture.

## Overview
The Universal Meta‑Lens System (UMLS) defines a single adaptive optical framework capable of supporting all human refractive deficiencies. Instead of manufacturing unique lens geometries per person, UMLS provides a universal envelope of optical, parallax, and neural‑comfort parameters that can be instantiated for any user.

The system integrates:
- Universal optical ranges (Sphere, Cylinder, Axis)
- Adaptive parallax offsets
- Eye‑velocity phase delay modeling
- Scroll‑stabilized depth perception
- A Deficiency Compensation Matrix (DCM) covering refractive, binocular, chromatic, and neural factors
- A material abstraction layer supporting CR‑39, polycarbonate, Trivex, and high‑index plastics

---

## Universal Optical Ranges
These ranges cover all human prescriptions.

### Sphere (SPH)
- **Range:** −12.00 D → +10.00 D  
- Supports full myopia and hyperopia correction.

### Cylinder (CYL)
- **Range:** −0.25 D → −6.00 D  
- Universal astigmatism correction range.

### Axis (AXIS)
- **Range:** 0° → 180°  
- Full rotational orientation for astigmatism.

---

## Adaptive Parallax Engine
A dynamic system that stabilizes depth perception using counter‑motion illusions.

### Parallax Offsets
- **x/y offset range:** 0.00 → 0.40 mm  
- **theta offset range:** 0.0° → 2.5°  
- **alpha (velocity gain):** 0.0005 → 0.005 mm/deg/s  
- **beta (gaze gain):** 0.0005 → 0.004 mm/deg  

### Eye‑Velocity Phase Delay
- **Base latency:** 2 → 8 ms  
- **k1 (velocity coefficient):** 0.005 → 0.030 ms/deg/s  
- **k2 (acceleration coefficient):** 0.001 → 0.010 ms/deg/s²  
- **Max perceptual latency:** 20 ms  

### Parallax Scroll Stabilization
- **γ (scroll gain):** 0.05 → 0.25  
- **δ (motion damping):** 0.002 → 0.010 mm/deg/s  
- **ζ (damping ratio):** 0.8 → 1.4  
- **Max binocular disparity:** 10 → 30 arcmin  

---

## Deficiency Compensation Matrix (DCM)
A 4×4 matrix encoding all corrective factors.

| Code | Meaning | Range |
|------|---------|--------|
| M | Myopia | −12 → +10 D |
| H | Hyperopia | −12 → +10 D |
| A | Astigmatism axis | 0 → 180° |
| S | Spherical | −12 → +10 D |
| C | Chromatic correction | 0.00 → 0.50 |
| T | Torsion | 0 → 5° |
| B | Binocular balance | 0 → 6Δ |
| P | Parallax sensitivity | 0.1 → 1.0 |
| V | Vergence support | 0 → 6Δ |
| N | Neural weighting | 0.1 → 1.0 |

---

## Material Layer
UMLS supports multiple materials.  
The cheapest viable option is **CR‑39**, a standard optical plastic.

### CR‑39 Properties
- Refractive Index: 1.498  
- Abbe Number: 58  
- Density: 1.32 g/cm³  
- Impact Resistance: Low  
- Scratch Resistance: Moderate  
- Cost: Lowest  
- Machinability: High  

---

## Instantiation Pipeline
Each user receives a personalized lens by filling the universal envelope with:
- Their prescription (SPH/CYL/AXIS)
- Eye‑tracking profile
- Neural comfort profile

The architecture remains universal; only the parameters change.

---

## Purpose
The Universal Meta‑Lens System is designed to:
- Replace individualized lens manufacturing
- Provide a single adaptive architecture
- Support all human refractive and binocular deficiencies
- Enable future parallax‑adaptive AR/VR optical systems
