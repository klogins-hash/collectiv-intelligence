#!/usr/bin/env python3
import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class AlignmentDimensions:
    """
    The 5 Dimensions of the Zion-Babylon Spectrum.
    Each dimension is scored from -10 (Babylon/Hell) to +10 (Zion/Heaven).
    """
    
    # 1. Voluntarism (The Gate)
    # -10: Slavery, Prison, Coercion, Iron Curtain (North Korea, Slavery)
    #   0: Contractual obligation, high friction exit (Gym membership, Citizenship)
    # +10: Radical Free Agency, Open Door, Voluntary Association (The Collectiv)
    entry_exit: float

    # 2. Governance (The Crown)
    # -10: Totalitarian Dictator, God-King, Fascism (Hitler, Putin, CCP)
    #   0: Representative Democracy, Corporate Board (USA, Public Company)
    # +10: Common Consent, Unanimous Voice, "One Heart One Mind" (Zion, DAO)
    governance: float

    # 3. Economics (The Purse)
    # -10: Hyper-Extraction, 1% Hoarding, Oligarchy (Bezos, Musk, Zuck)
    #   0: Mixed Economy, Middle Class (Traditional Capitalism)
    # +10: "No Poor Among Them", Consecration, Circular Wealth (Cooperative)
    economics: float

    # 4. Agency (The Soul)
    # -10: Manipulation, Brainwashing, Algorithmic Control (Meta, TikTok)
    #   0: Neutral Service, Utility (ISP, Water Company)
    # +10: Sovereignty, Expansion of Capability, Education (The Collectiv)
    agency: float

    # 5. Culture (The Spirit)
    # -10: Hate, Division, War, "Dog Eat Dog" (Twitter/X, War Zones)
    #   0: Tolerance, Coexistence (Modern City)
    # +10: Righteousness, Unity, "Dwelt in Righteousness" (Utopia)
    culture: float

    def calculate_total(self) -> float:
        """Returns the total Alignment Score from -100% to +100%."""
        raw_sum = (
            self.entry_exit + 
            self.governance + 
            self.economics + 
            self.agency + 
            self.culture
        )
        # Max possible sum is 50. Min is -50.
        # Multiply by 2 to get percentage.
        return raw_sum * 2

class AlignmentScorer:
    def __init__(self):
        self.benchmarks = {}

    def add_entity(self, name: str, dims: AlignmentDimensions):
        score = dims.calculate_total()
        self.benchmarks[name] = {
            "score": score,
            "breakdown": dims.__dict__
        }

    def print_report(self):
        print(f"{'ENTITY':<25} | {'SCORE':<10} | {'VERDICT'}")
        print("-" * 60)
        
        sorted_entities = sorted(self.benchmarks.items(), key=lambda x: x[1]['score'], reverse=True)
        
        for name, data in sorted_entities:
            score = data['score']
            if score >= 80: verdict = "ZION (Utopia)"
            elif score >= 20: verdict = "Free Society"
            elif score >= -20: verdict = "Mixed/Neutral"
            elif score >= -80: verdict = "Extractive (Babylon)"
            else: verdict = "DYSTOPIA (Hell)"
            
            print(f"{name:<25} | {score:>+5.1f}%    | {verdict}")

def main():
    scorer = AlignmentScorer()

    # --- THE ZION POLE (+100%) ---
    scorer.add_entity("The Collectiv (Ideal)", AlignmentDimensions(
        entry_exit=10,  # Voluntary joining/leaving
        governance=10,  # One heart one mind
        economics=10,   # No poor among them
        agency=10,      # Expanding agency
        culture=10      # Dwelt in righteousness
    ))

    # --- THE BABYLON POLE (-100%) ---
    scorer.add_entity("Totalitarian State (NK)", AlignmentDimensions(
        entry_exit=-10, # Cannot leave (death)
        governance=-10, # Dictator (Kim)
        economics=-10,  # Starvation vs Elite
        agency=-10,     # Total mind control
        culture=-10     # Fear/Coercion
    ))

    scorer.add_entity("Nazi Germany (1940)", AlignmentDimensions(
        entry_exit=-10,
        governance=-10, # Hitler
        economics=-8,   # War economy
        agency=-10,     # Genocide
        culture=-10     # Hate
    ))

    # --- THE EXTRACTIVS (Tech Oligarchs) ---
    scorer.add_entity("Meta (Zuckerberg)", AlignmentDimensions(
        entry_exit=2,   # Can leave, but network effects coerce
        governance=-8,  # Shareholder dictatorship (Zuck controls votes)
        economics=-9,   # Ad model extracts attention for profit
        agency=-8,      # Algorithms manipulate behavior
        culture=-5      # Optimizes for outrage/division
    ))

    scorer.add_entity("Amazon (Bezos Era)", AlignmentDimensions(
        entry_exit=4,   # Convenient, voluntary
        governance=-7,  # Corporate hierarchy
        economics=-9,   # Crushes small biz, warehouse conditions
        agency=-2,      # Consumerism
        culture=-3      # Efficiency over humanity
    ))

    scorer.add_entity("X (Elon Musk)", AlignmentDimensions(
        entry_exit=5,   # Voluntary
        governance=-9,  # "Free speech absolutist" (Monarch)
        economics=-5,   # Ad/Sub model
        agency=2,       # Gives voice, but algorithmic chaos
        culture=-6      # Polarizing
    ))

    # --- POLITICAL FIGURES ---
    scorer.add_entity("Putin's Russia", AlignmentDimensions(
        entry_exit=-6,  # Hard to leave, dissidents killed
        governance=-10, # Autocracy
        economics=-8,   # Oligarchy
        agency=-9,      # State media control
        culture=-7      # Nationalism/War
    ))

    scorer.add_entity("Trumpism (MAGA)", AlignmentDimensions(
        entry_exit=5,   # Voluntary movement
        governance=-6,  # Strongman tendency
        economics=-4,   # Deregulation/Tax cuts for wealthy
        agency=2,       # "Anti-woke" agency? (Debatable)
        culture=-8      # Divisive rhetoric
    ))

    # --- RUN REPORT ---
    scorer.print_report()

if __name__ == "__main__":
    main()
