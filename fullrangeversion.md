# Universal Meta-Lens v2 — Full Range Version
# Includes complete universal ranges for all optical & parallax variables

UNIVERSAL_META_LENS_V2 = {
    "Optics_Core": {
        "Nominal_Diameter_mm": 70,                     # Universal lens blank size
        "Center_Thickness_mm": 2.0,                    # Typical center thickness

        "Base_Radius_of_Curvature_mm": {
            "value": 7.8,
            "tolerance_mm": 0.3,
            "universal_range_mm": [6.5, 9.0],          # Covers all SPH powers from -12 to +10
            "note": "Universal curvature envelope for all refractive errors."
        },

        "Refractive_Index": {
            "material_n": 1.62,
            "universal_range_n": [1.50, 1.74],         # All commercial high-index materials
            "wavelength_nm": 550,
            "Abbe_Number": 42,
            "Abbe_range": [30, 58]                     # Low-dispersion to high-dispersion materials
        },

        "Back_Surface_Power_Diopters": {
            "range_D": [-12.00, +10.00],               # Full human prescription range
            "step_D": 0.25,
            "note": "Universal dioptric range for myopia, hyperopia, presbyopia."
        }
    },

    "Adaptive_Parallax_Offsets": {
        "base_vector": {
            "x_delta_mm": 0.10,
            "y_delta_mm": 0.08,
            "theta_delta_deg": 0.7
        },

        "universal_ranges": {
            "x_delta_mm_range": [0.00, 0.40],          # Full safe parallax offset envelope
            "y_delta_mm_range": [0.00, 0.40],
            "theta_delta_deg_range": [0.0, 2.5]
        },

        "dynamic_adjustment": {
            "formula": "P_dyn = P_base + α * eye_velocity + β * gaze_angle",
            "alpha_mm_per_deg_per_s": 0.002,
            "beta_mm_per_deg": 0.0015,

            "alpha_range": [0.0005, 0.005],            # Slow → fast saccadic profiles
            "beta_range": [0.0005, 0.004],             # Narrow → wide gaze-angle users

            "note": "Adaptive offsets scale with eye motion and gaze geometry."
        },

        "constraints": {
            "max_offset_mm": 0.35,
            "max_theta_deg": 2.0,
            "universal_max_offset_range_mm": [0.20, 0.50],
            "note": "Hard caps to avoid distortion, nausea, or fusion instability."
        }
    },

    "Eye_Velocity_Phase_Delay": {
        "base_latency_ms": 4.0,
        "base_latency_range_ms": [2.0, 8.0],           # Human perceptual comfort envelope

        "nonlinear_component": {
            "formula": "RPD = L0 + k1 * |eye_velocity| + k2 * |eye_acceleration|",
            "L0_ms": 4.0,
            "k1_ms_per_deg_per_s": 0.015,
            "k2_ms_per_deg_per_s2": 0.003,

            "k1_range": [0.005, 0.030],                # Slow → fast movers
            "k2_range": [0.001, 0.010]                 # Low → high acceleration profiles
        },

        "perceptual_bounds_ms": {
            "max_latency_ms": 20.0,
            "target_latency_ms": 10.0,
            "universal_latency_range_ms": [5.0, 20.0],
            "note": "Latency kept below perceptual instability threshold."
        }
    },

    "Parallax_Scroll_Stabilization": {
        "scroll_rate": {
            "formula": "PSR = γ * P_dyn - δ * eye_velocity",
            "gamma_per_s": 0.12,
            "delta_mm_per_deg_per_s": 0.004,

            "gamma_range": [0.05, 0.25],               # Low → high scroll responsiveness
            "delta_range": [0.002, 0.010]              # Low → high motion damping
        },

        "damping": {
            "type": "critical_damping",
            "zeta": 1.0,
            "zeta_range": [0.8, 1.4],                  # Under → over-damped safe range
            "note": "Controls oscillation in perceived depth."
        },

        "fusion_constraints": {
            "max_disparity_arcmin": 20,
            "universal_disparity_range_arcmin": [10, 30],
            "note": "Keeps binocular fusion stable for all users."
        }
    },

    "Deficiency_Compensation_Matrix_V2": {
        "structure": [
            ["M", "A", "H", "B"],
            ["A", "C", "T", "P"],
            ["H", "T", "S", "V"],
            ["B", "P", "V", "N"]
        ],

        "universal_ranges": {
            "M_range_D": [-12.00, +10.00],             # Myopia / hyperopia
            "H_range_D": [-12.00, +10.00],
            "A_axis_range_deg": [0, 180],              # Full astigmatism axis
            "S_sphere_range_D": [-12.00, +10.00],
            "C_chromatic_range": [0.00, 0.50],         # Chromatic aberration compensation
            "T_torsion_range_deg": [0.0, 5.0],         # Torsional misalignment
            "B_binocular_prism_range": [0.0, 6.0],     # Phoria / prism correction
            "P_parallax_sensitivity_range": [0.1, 1.0],
            "V_vergence_prism_range": [0.0, 6.0],
            "N_neural_weighting_range": [0.1, 1.0]
        },

        "note": "DCM covers all human refractive, binocular, chromatic, and neural comfort profiles."
    }
}
