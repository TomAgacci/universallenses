# Universal Reading Portion Specification
# Person-agnostic, gradient-capable reading lens architecture

UNIVERSAL_READING_PORTION = {
    "Reading_Power": {
        "base_add_D": 0.00,                     # No add by default
        "universal_add_range_D": [0.75, 3.50],  # Covers all typical reading needs
        "step_D": 0.25,
        "description": "Universal reading-add envelope for near vision."
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
        "near_range_cm": [25, 40],              # Typical book/phone distance
        "intermediate_range_cm": [40, 70],      # Monitor / tablet distance
        "description": "Universal near and intermediate reading distances."
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
    }
}
