from typing import Dict


class RecommendationEngine:
    """Generate simple farming recommendations based on inputs and predicted crop."""

    def __init__(self):
        # crop-specific simple notes; these can be expanded.
        self.crop_notes = {
            "rice": "Requires high water; prefers flooded conditions and moderate pH.",
            "maize": "Prefers well-drained soils and moderate rainfall.",
            "chickpea": "Thrives in well-drained soils with low to moderate rainfall.",
        }

    def _nutrient_advice(self, inputs: Dict[str, float]):
        adv = []
        if inputs["N"] < 50:
            adv.append("Increase Nitrogen: consider applying urea or organic compost.")
        elif inputs["N"] > 250:
            adv.append("Avoid excess Nitrogen to prevent excessive vegetative growth.")

        if inputs["P"] < 20:
            adv.append("Add Phosphorus: use rock phosphate or single superphosphate.")

        if inputs["K"] < 100:
            adv.append("Add Potassium: muriate of potash or potash-rich organic fertilizers.")

        return adv

    def _water_advice(self, inputs: Dict[str, float]):
        adv = []
        if inputs["rainfall"] < 50:
            adv.append("Irrigation needed: consider drip or sprinkler scheduling.")
        elif inputs["rainfall"] > 500:
            adv.append("Reduce irrigation and improve drainage to avoid waterlogging.")
        return adv

    def _ph_advice(self, inputs: Dict[str, float]):
        adv = []
        if inputs["ph"] < 5.5:
            adv.append("Soil is acidic: apply lime to raise pH.")
        elif inputs["ph"] > 7.8:
            adv.append("Soil is alkaline: consider sulfur or acidifying amendments.")
        return adv

    def generate(self, predicted_crop: str, inputs: Dict[str, float]) -> str:
        notes = []
        crop = predicted_crop.lower() if isinstance(predicted_crop, str) else str(predicted_crop)
        if crop in self.crop_notes:
            notes.append(self.crop_notes[crop])
        else:
            notes.append(f"{predicted_crop} is a suitable choice based on model prediction.")

        notes.extend(self._nutrient_advice(inputs))
        notes.extend(self._water_advice(inputs))
        notes.extend(self._ph_advice(inputs))

        if len(notes) == 0:
            return "No specific recommendations. Monitor soil and weather regularly."

        return " ".join(notes)
