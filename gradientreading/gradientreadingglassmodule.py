# Gradient Reading Glasses Module
# Adjustable reading-power system compatible with Universal Meta-Lens architecture

GRADIENT_READING_GLASSES = {
    "Reading_Mode": {
        "description": "Defines how reading power is distributed across the lens.",
        "modes": {
            "uniform": "Same reading power across entire lens.",
            "vertical_gradient": "Reading power increases from top → bottom.",
            "center_focus": "Reading power strongest at center, weaker outward.",
            "custom_profile": "User-defined gradient curve."
        }
    },

    "Reading_Power": {
        "base_add_D": 0.00,                     # No reading boost by default
        "adjustable_range_D": [0.75, 3.50],     # Universal reading-add range
        "step_D": 0.25,                         # Standard reading increments
        "description": "Universal range for reading enhancement."
    },

    "Gradient_Profile": {
        "vertical_gradient": {
            "top_zone_add_D": 0.00,             # Distance vision at top
            "bottom_zone_add_D": 2.50,          # Full reading power at bottom
            "gradient_curve": "linear",         # linear, quadratic, spline
            "note": "Classic progressive-style gradient."
        },

        "center_focus": {
            "center_add_D": 2.00,
            "peripheral_add_D": 0.50,
            "falloff_function": "gaussian",     # smooth drop-off
            "note": "Ideal for tablet/phone reading."
        },

        "custom_profile": {
            "user_defined_curve": "<function>",
            "allowed_shapes": ["linear", "spline", "sigmoid", "gaussian"],
            "constraints": {
                "max_add_D": 3.50,
                "min_add_D": 0.00
            }
        }
    },

    "Adaptive_Adjustment": {
        "auto_tune": True,
        "eye_tracking_integration": True,
        "parameters": {
            "reading_distance_cm_range": [25, 60],   # Universal near-focus range
            "head_tilt_compensation_deg": [-15, +15],
            "gaze_zone_detection": True
        },
        "description": "Automatically adjusts reading power based on gaze and distance."
    },

    "Material_Compatibility": {
        "CR39": {
            "supported": True,
            "notes": "Cheapest material; ideal for gradient reading lenses."
        },
        "Polycarbonate": {
            "supported": True,
            "notes": "Impact-resistant; good for active users."
        },
        "High_Index": {
            "supported": True,
            "notes": "Thinner lenses for high prescriptions."
        }
    },

    "Universal_Ranges": {
        "Sphere_D": [-12.00, +10.00],
        "Cylinder_D": [-0.25, -6.00],
        "Axis_deg": [0, 180],
        "Add_D": [0.75, 3.50],                   # Reading power range
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
