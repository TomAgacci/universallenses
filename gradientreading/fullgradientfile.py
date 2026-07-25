# Universal Gradient Reading Lens Module
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)
# You are free to share and adapt this file as long as attribution is provided.

UNIVERSAL_GRADIENT_READING_LENS = {
    "License": "CC BY 4.0",
    "License_URL": "https://creativecommons.org/licenses/by/4.0/",

    "Reading_Power": {
        "base_add_D": 0.00,
        "universal_add_range_D": [0.75, 3.50],
        "step_D": 0.25,
        "description": "Universal reading-add envelope covering all near-vision needs."
    },

    "Reading_Modes": {
        "uniform": {
            "description": "Same reading power across entire lens.",
            "add_range_D": [0.75, 3.50]
        },
        "vertical_gradient": {
            "description": "Distance at top, reading at bottom.",
            "top_zone_add_D_range": [0.00, 1.00],
            "middle_zone_add_D_range": [0.50, 2.50],
            "bottom_zone_add_D_range": [1.50, 3.50]
        },
        "center_focus": {
            "description": "Strong reading at center, weaker toward edges.",
            "center_add_D_range": [1.00, 3.50],
            "peripheral_add_D_range": [0.00, 1.50]
        },
        "custom_profile": {
            "description": "User-defined gradient curve.",
            "allowed_shapes": ["linear", "spline", "sigmoid", "gaussian"],
            "constraints": {
                "max_add_D": 3.50,
                "min_add_D": 0.00
            }
        }
    },

    "Universal_Gradient_Zones": {
        "zones": ["top", "middle", "bottom", "center", "periphery"],
        "vertical_layout": {
            "top": "distance / low add",
            "middle": "intermediate / medium add",
            "bottom": "near / high add"
        },
        "radial_layout": {
            "center": "near / high add",
            "periphery": "distance / low add"
        }
    },

    "Universal_Reading_Distances_cm": {
        "near_range_cm": [25, 40],
        "intermediate_range_cm": [40, 70],
        "description": "Universal near and intermediate reading distances."
    },

    "Adaptive_Adjustment": {
        "auto_tune": True,
        "eye_tracking_integration": True,
        "parameters": {
            "reading_distance_cm_range": [25, 60],
            "head_tilt_compensation_deg": [-15, +15],
            "gaze_zone_detection": True
        },
        "description": "Automatically adjusts reading power based on gaze and distance."
    },

    "Material_Compatibility": {
        "CR39": {
            "supported": True,
            "note": "Cheapest universal reading lens material."
        },
        "Polycarbonate": {
            "supported": True,
            "note": "Impact-resistant option."
        },
        "High_Index": {
            "supported": True,
            "note": "Thin lenses for high prescriptions."
        }
    },

    "Universal_Ranges": {
        "Sphere_D": [-12.00, +10.00],
        "Cylinder_D": [-0.25, -6.00],
        "Axis_deg": [0, 180],
        "Add_D": [0.75, 3.50],
        "Gradient_Zones": ["top", "middle", "bottom", "center", "periphery"]
    },

    "Generate_Profile_Function": """
def generate_gradient_profile(mode, add_power):
    if mode == 'uniform':
        return {'top': add_power, 'middle': add_power, 'bottom': add_power}

    if mode == 'vertical_gradient':
        return {
            'top': 0.00,
            'middle': add_power * 0.5,
            'bottom': add_power
        }

    if mode == 'center_focus':
        return {
            'center': add_power,
            'periphery': add_power * 0.25
        }

    if mode == 'custom_profile':
        raise NotImplementedError('Custom profile must be supplied by user.')

    raise ValueError('Invalid gradient mode.')
"""
}
