# -*- coding: utf-8 -*-
"""BUN & Creatinine Hydration Sentinel for GenPark Personal Agent."""
import json
from typing import Dict, Any

class BUNCreatinineHydrationSentinel:
    @staticmethod
    def calculate_bun_creatinine_ratio(bun_mg_dl: float, creatinine_mg_dl: float, egfr_ml_min: float = 90.0) -> Dict[str, Any]:
        ratio = round(bun_mg_dl / max(0.1, creatinine_mg_dl), 1)
        if ratio > 20.0:
            status = "PRERENAL_AZOTEMIA_DEHYDRATION"
            assessment = "Elevated ratio indicates significant intravascular volume contraction or high catabolic protein breakdown."
        elif ratio < 10.0:
            status = "LOW_RATIO_HEPATIC_OR_MALNUTRITION"
            assessment = "Low ratio suggests acute tubular necrosis, low protein intake, or overhydration."
        else:
            status = "PHYSIOLOGICAL_OPTIMAL"
            assessment = "Normal balanced renal perfusion and baseline hydration."
            
        return {
            "bun_mg_dl": bun_mg_dl,
            "creatinine_mg_dl": creatinine_mg_dl,
            "bun_creatinine_ratio": ratio,
            "egfr_ml_min": egfr_ml_min,
            "hydration_classification": status,
            "clinical_guidance": assessment
        }

    @staticmethod
    def prescribe_rehydration_fluid_remedy(ratio: float, body_weight_kg: float) -> Dict[str, Any]:
        fluid_target_ml = round(body_weight_kg * 35.0, 0)
        if ratio > 20.0:
            fluid_target_ml += 1000.0  # Extra liter for prerenal dehydration
            advisory = "Incorporate 1g sodium chloride and 300mg potassium citrate to restore intravascular oncotic pressure."
        else:
            advisory = "Maintain baseline isotonic fluid hydration."
        return {
            "target_daily_fluid_intake_ml": fluid_target_ml,
            "electrolyte_enrichment": advisory,
            "monitoring_directive": "Re-check serum electrolytes and urine specific gravity after 48 hours."
        }
