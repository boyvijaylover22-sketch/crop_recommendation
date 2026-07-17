<<<<<<< HEAD
=======
"""Generate beginner-friendly farming recommendations."""

from __future__ import annotations

>>>>>>> 05f08e4 (Initial Smart Farming AI assistant)
from typing import Dict


class RecommendationEngine:
<<<<<<< HEAD
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
=======
    """Create practical advice based on predicted crop and input conditions."""

    def generate_recommendations(self, crop: str, inputs_data: Dict[str, float]) -> Dict[str, str]:
        """Return a set of recommendations for the predicted crop."""
        crop_name = crop.lower()
        temperature = inputs_data["Temperature"]
        humidity = inputs_data["Humidity"]
        rainfall = inputs_data["Rainfall"]
        ph = inputs_data["pH"]
        nitrogen = inputs_data["Nitrogen"]
        phosphorus = inputs_data["Phosphorus"]
        potassium = inputs_data["Potassium"]

        recommendations: Dict[str, str] = {}
        recommendations["soil_improvement"] = self._soil_tip(nitrogen, phosphorus, potassium, ph)
        recommendations["irrigation"] = self._irrigation_tip(rainfall, humidity, temperature)
        recommendations["fertilizer"] = self._fertilizer_tip(crop_name, nitrogen, potassium)
        recommendations["crop_care"] = self._crop_care_tip(crop_name, temperature, humidity)
        return recommendations

    def explain_crop_suitability(self, crop: str, inputs_data: Dict[str, float]) -> str:
        """Explain why the crop is suitable for the provided conditions."""
        temperature = inputs_data["Temperature"]
        rainfall = inputs_data["Rainfall"]
        ph = inputs_data["pH"]
        humidity = inputs_data["Humidity"]
        return (
            f"{crop} is well suited because the provided conditions show a balanced environment "
            f"with temperature {temperature}°C, humidity {humidity}%, rainfall {rainfall} mm, "
            f"and pH {ph}."
        )

    def _soil_tip(self, nitrogen: float, phosphorus: float, potassium: float, ph: float) -> str:
        if nitrogen < 80:
            return "Consider adding compost or nitrogen-rich organic matter to strengthen plant growth."
        if ph < 6.0:
            return "Apply lime to raise soil pH and improve nutrient availability."
        if potassium < 80:
            return "Add potassium-rich fertilizer to improve root strength and disease resistance."
        return "Soil conditions look balanced; maintain organic matter and monitor nutrient levels."

    def _irrigation_tip(self, rainfall: float, humidity: float, temperature: float) -> str:
        if rainfall > 150 and humidity > 70:
            return "Reduce irrigation because rainfall and humidity are already sufficient."
        if temperature > 35:
            return "Increase irrigation frequency during hot conditions to prevent water stress."
        return "Maintain steady soil moisture and irrigate when the topsoil begins to dry."

    def _fertilizer_tip(self, crop_name: str, nitrogen: float, potassium: float) -> str:
        if crop_name in {"rice", "wheat", "maize"}:
            return "Use a balanced NPK fertilizer and monitor nutrient uptake closely."
        if nitrogen < 60:
            return "Add a nitrogen-based fertilizer to support healthy leaf and stem development."
        if potassium < 80:
            return "Use potassium fertilizer to improve general vigor and resilience."
        return "Apply a light, balanced fertilizer and avoid overfeeding the crop."

    def _crop_care_tip(self, crop_name: str, temperature: float, humidity: float) -> str:
        if crop_name in {"rice", "maize"}:
            return "Watch for fungal diseases in humid weather and ensure good airflow around plants."
        if humidity > 80:
            return "Monitor for pests and disease pressure during high-humidity periods."
        if temperature > 30:
            return "Provide shade and mulch to reduce heat stress."
        return "Maintain regular field inspection and remove weeds promptly."
>>>>>>> 05f08e4 (Initial Smart Farming AI assistant)
