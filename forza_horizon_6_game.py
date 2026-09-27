from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import OptionSet, Toggle, DefaultOnToggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class ForzaHorizon6ArchipelagoOptions:
    forza_horizon_6_car_set: ForzaHorizon6IncludeCarSet
    forza_horizon_6_challenge_type: ForzaHorizon6IncludeChallengeType
    forza_horizon_6_condition_type: ForzaHorizon6IncludeConditionType
    forza_horizon_6_use_car_list: ForzaHorizon6IncludeMyCarList
    forza_horizon_6_car_list: ForzaHorizon6MyCarList
    
class ForzaHorizon6Game(Game):
    name = "Forza Horizon 6"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
        KeymastersKeepGamePlatforms.PS5,
    ]

    is_adult_only_or_unrated = False

    options_cls = ForzaHorizon6ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Set Drivatar Difficulty to DIFFICULTY",
                data={
                    "DIFFICULTY": (self.drivatar_difficulties, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Set Camera View to CAMERA",
                data={
                    "CAMERA": (self.cameras, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Set Driving Assists Difficulty to DIFFICULTY",
                data={
                    "DIFFICULTY": (self.assists, 1),
                },
            ),
            GameObjectiveTemplate(
                label="ASSIST",
                data={
                    "ASSIST": (self.assists_single, 1),
                },
            ),
            GameObjectiveTemplate(
                label="ASSIST and set Drivatar Difficulty to DIFFICULTY",
                data={
                    "ASSIST": (self.assists_single, 1),
                    "DIFFICULTY": (self.drivatar_difficulties, 1),
                },
            ),
            GameObjectiveTemplate(
                label="You cannot fast travel to your destinations",
                data={},
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = []
        
        if "Single Race" in self.challenge_sets:
            Empty = True

            templates.extend([
                GameObjectiveTemplate(
                    label="Finish 1st on TRACK touge",
                    data={
                        "TRACK": (self.tracks_touge, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ])
            # Opp Num, Weather, Time of Day, Lap, Traffic

            if "Brand" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACK with a car from the following brand: BRAND",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACK": (self.tracks_including_long, 1),
                            "BRAND": (self.car_brands, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                ])

            if "Class" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACK with a car from the following class: CLASS",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACK": (self.tracks_including_long, 1),
                            "CLASS": (self.car_classes, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                ])

            if "Type" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACK with a car from the following type: TYPE",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACK": (self.tracks_including_long, 1),
                            "TYPE": (self.car_types, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                ])

            if "Car" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACK with the following car: CAR",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACK": (self.tracks_including_long, 1),
                            "CAR": (self.cars, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=4,
                    ),
                ])

            if Empty:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACK",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACK": (self.tracks_including_long, 1)
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=4,
                    ),
                ])

        if "Triple Race" in self.challenge_sets:
            Empty = True

            if "Brand" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACKS with the following brand: BRAND",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACKS": (self.tracks, 3),
                            "BRAND": (self.car_brands, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=4,
                    ),
                ])
                
            if "Class" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACKS with a car from the following class: CLASS",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACKS": (self.tracks, 3),
                            "CLASS": (self.car_classes, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=2,
                    ),
                ])

            if "Type" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACKS with a car from the following type: TYPE",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACKS": (self.tracks, 3),
                            "TYPE": (self.car_types, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=2,
                    ),
                ])

            if "Car" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACKS with the following car: CAR",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACKS": (self.tracks, 3),
                            "CAR": (self.cars, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=4,
                    ),
                ])

            if Empty:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACKS",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACKS": (self.tracks, 3)
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=4,
                    ),
                ])

        if "Custom Race" in self.challenge_sets:
            Empty = True
            # Opp Num, Weather, Time of Day, Lap, Traffic

            if "Brand" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACK (OPP opponents, LAP laps, WHEATHER weather, TIME, TRAFFIC) with a car from the following brand: BRAND",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACK": (self.tracks_including_long, 1),
                            "OPP": (self.opp_number, 1),
                            "LAP": (self.lap_number, 1),
                            "WEATHER": (self.weather, 1),
                            "TIME": (self.time, 1),
                            "TRAFFIC": (self.traffic, 1),
                            "BRAND": (self.car_brands, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                ])

            if "Class" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACK (OPP opponents, LAP laps, WHEATHER weather, TIME, TRAFFIC) with a car from the following class: CLASS",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACK": (self.tracks_including_long, 1),
                            "OPP": (self.opp_number, 1),
                            "LAP": (self.lap_number, 1),
                            "WEATHER": (self.weather, 1),
                            "TIME": (self.time, 1),
                            "TRAFFIC": (self.traffic, 1),
                            "CLASS": (self.car_classes, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                ])

            if "Type" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACK (OPP opponents, LAP laps, WHEATHER weather, TIME, TRAFFIC) with a car from the following type: TYPE",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACK": (self.tracks_including_long, 1),
                            "OPP": (self.opp_number, 1),
                            "LAP": (self.lap_number, 1),
                            "WEATHER": (self.weather, 1),
                            "TIME": (self.time, 1),
                            "TRAFFIC": (self.traffic, 1),
                            "TYPE": (self.car_types, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                ])

            if "Car" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACK (OPP opponents, LAP laps, WHEATHER weather, TIME, TRAFFIC) with a car from the following car: CAR",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACK": (self.tracks_including_long, 1),
                            "OPP": (self.opp_number, 1),
                            "LAP": (self.lap_number, 1),
                            "WEATHER": (self.weather, 1),
                            "TIME": (self.time, 1),
                            "TRAFFIC": (self.traffic, 1),
                            "CAR": (self.cars, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=4,
                    ),
                ])

            if Empty:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Finish PLACEMENT on TRACK (OPP opponents, LAP laps, WHEATHER weather, TIME, TRAFFIC)",
                        data={
                            "PLACEMENT": (self.race_placements, 1),
                            "TRACK": (self.tracks_including_long, 1),
                            "OPP": (self.opp_number, 1),
                            "LAP": (self.lap_number, 1),
                            "WEATHER": (self.weather, 1),
                            "TIME": (self.time, 1),
                            "TRAFFIC": (self.traffic, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=4,
                    ),
                ])


        if "Rival" in self.challenge_sets: 
            templates.extend([
                GameObjectiveTemplate(
                    label="Post a clean time on the Monthly Rival leaderboard",
                    data={},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Beat your closest rival on the Monthly Rival leaderboard",
                    data={},
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
            ])
            Empty = True
                
            if "Class" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Post a clean time on the Rivals leaderboard for TRACK with CLASS car",
                        data={
                            "TRACK": (self.tracks_including_long, 1),
                            "CLASS": (self.car_classes_alternate, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                    GameObjectiveTemplate(
                        label="Beat your closest rival on the Rivals leaderboard for TRACK with CLASS car",
                        data={
                            "TRACK": (self.tracks_including_long, 1),
                            "CLASS": (self.car_classes_alternate, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=3,
                    ),
                ])

            if "Car" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Post a clean time on the Rivals leaderboard for TRACK with the following car : CAR",
                        data={
                            "TRACK": (self.tracks_including_long, 1),
                            "CAR": (self.cars, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=3,
                    ),
                    GameObjectiveTemplate(
                        label="Beat your closest rival on the Rivals leaderboard for TRACK with the following car : CAR",
                        data={
                            "TRACK": (self.tracks_including_long, 1),
                            "CAR": (self.cars, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=3,
                    ),
                ])

            if Empty:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Post a clean time on the Rivals leaderboard for TRACK",
                        data={
                            "TRACK": (self.tracks_including_long, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=3,
                    ),
                    GameObjectiveTemplate(
                        label="Beat your closest rival on the Rivals leaderboard for TRACK",
                        data={
                            "TRACK": (self.tracks_including_long, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=3,
                    ),
                ])

        if "PR Stunt" in self.challenge_sets: 
            templates.extend([
                GameObjectiveTemplate(
                    label="Get at least STAR stars on the following PR Stunts: PR_STUNTS",
                    data={
                        "STAR": (self.star_amount_range, 1),
                        "PR_STUNTS": (self.pr_stunts, 3),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Get at least STAR stars on the following PR Stunts: PR_STUNTS",
                    data={
                        "STAR": (self.star_amount_range, 1),
                        "PR_STUNTS": (self.pr_stunts, 5),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        if "Skill" in self.challenge_sets: 
            templates.extend([
                GameObjectiveTemplate(
                    label="Pull off the following Skills: SKILLS",
                    data={
                        "SKILLS": (self.skills, 3),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Pull off the following Skills: SKILLS",
                    data={
                        "SKILLS": (self.skills, 5),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        if "Car Mastery" in self.challenge_sets: 
            Empty = True

            if "Brand" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Complete the Mastery Tree of a car from the following brand: BRAND",
                        data={
                            "BRAND": (self.car_brands, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=1,
                    ),
                ])
                
            if "Class" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Complete the Mastery Tree of a car from the following class: CLASS",
                        data={
                            "CLASS": (self.car_classes, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=1,
                    ),
                ])

            if "Type" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Complete the Mastery Tree of a car from the following type: TYPE",
                        data={
                            "TYPE": (self.car_types, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=1,
                    )
                ])

            if "Car" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Complete the Mastery Tree of the following car: CAR",
                        data={
                            "CAR": (self.cars, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=2,
                    )
                ])

            if Empty:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Complete the Mastery Tree",
                        data={},
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=2,
                    )
                ])

        if "Gift" in self.challenge_sets: 
            templates.extend([
                GameObjectiveTemplate(
                    label="Gift a car",
                    data={},
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                )
            ])

        if "Online Round" in self.challenge_sets: 
            templates.extend([
                GameObjectiveTemplate(
                    label="Play a round of ONLINE",
                    data={
                        "ONLINE": (self.online_modes, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
            ])

        if "Cruise" in self.challenge_sets: 
            Empty = True

            if "Brand" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Drive from LOC1 to LOC2 with a car from the following brand: BRAND",
                        data={
                            "LOC1": (self.locations, 1),
                            "LOC2": (self.locations, 1),
                            "BRAND": (self.car_brands, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                    GameObjectiveTemplate(
                        label="Drive from LOC1 to LOC2 using ANNA's autodrive with the following brand: BRAND",
                        data={
                            "LOC1": (self.locations, 1),
                            "LOC2": (self.locations, 1),
                            "BRAND": (self.car_brands, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                ])
                
            if "Class" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Drive from LOC1 to LOC2 with a car from the following class: CLASS",
                        data={
                            "LOC1": (self.locations, 1),
                            "LOC2": (self.locations, 1),
                            "CLASS": (self.car_classes, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                    GameObjectiveTemplate(
                        label="Drive from LOC1 to LOC2 using ANNA's autodrive with the following class: CLASS",
                        data={
                            "LOC1": (self.locations, 1),
                            "LOC2": (self.locations, 1),
                            "CLASS": (self.car_classes, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                ])

            if "Type" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Drive from LOC1 to LOC2 with a car from the following type: TYPE",
                        data={
                            "LOC1": (self.locations, 1),
                            "LOC2": (self.locations, 1),
                            "TYPE": (self.car_types, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                    GameObjectiveTemplate(
                        label="Drive from LOC1 to LOC2 using ANNA's autodrive with the following type: TYPE",
                        data={
                            "LOC1": (self.locations, 1),
                            "LOC2": (self.locations, 1),
                            "TYPE": (self.car_types, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                ])

            if "Car" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Drive from LOC1 to LOC2 with the following car: CAR",
                        data={
                            "LOC1": (self.locations, 1),
                            "LOC2": (self.locations, 1),
                            "CAR": (self.cars, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                    GameObjectiveTemplate(
                        label="Drive from LOC1 to LOC2 using ANNA's autodrive with the following car: CAR",
                        data={
                            "LOC1": (self.locations, 1),
                            "LOC2": (self.locations, 1),
                            "CAR": (self.cars, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                ])

            if Empty:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Drive from LOC1 to LOC2",
                        data={
                            "LOC1": (self.locations, 1),
                            "LOC2": (self.locations, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                    GameObjectiveTemplate(
                        label="Drive from LOC1 to LOC2 using ANNA's autodrive",
                        data={
                            "LOC1": (self.locations, 1),
                            "LOC2": (self.locations, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    ),
                ])

        if "Job" in self.challenge_sets: 
            templates.extend([
                GameObjectiveTemplate(
                    label="Get at least STAR stars on a job shift",
                    data={
                        "STAR": (self.star_amount_job_range, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Finish JOB job shift",
                    data={
                        "JOB": (self.star_amount_range, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                )
            ])

        if "Story" in self.challenge_sets: 
            templates.extend([
                GameObjectiveTemplate(
                    label="Get at least STAR stars on the following Story Chapter: STORY",
                    data={
                        "STAR": (self.star_amount_range, 1),
                        "STORY": (self.stories, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        if "Time Attack" in self.challenge_sets:
            Empty = True

            if "Brand" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Complete LAP laps on TA with a car from the following brand: BRAND",
                        data={
                            "LAP": (self.time_attack_lap_range, 1),
                            "TA": (self.time_attack, 1),
                            "BRAND": (self.car_brands, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=1,
                    ),
                ])
                
            if "Class" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Complete LAP laps on TA with a car from the following class: CLASS",
                        data={
                            "LAP": (self.time_attack_lap_range, 1),
                            "TA": (self.time_attack, 1),
                            "CLASS": (self.car_classes, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=1,
                    ),
                ])

            if "Type" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Complete LAP laps on TA with a car from the following type: TYPE",
                        data={
                            "LAP": (self.time_attack_lap_range, 1),
                            "TA": (self.time_attack, 1),
                            "TYPE": (self.car_types, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=1,
                    ),
                ])

            if "Car" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Complete LAP laps on TA with the following car: CAR",
                        data={
                            "LAP": (self.time_attack_lap_range, 1),
                            "TA": (self.time_attack, 1),
                            "CAR": (self.cars, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=1,
                    ),
                ])

            if Empty:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Complete LAP laps on TA",
                        data={
                            "LAP": (self.time_attack_lap_range, 1),
                            "TA": (self.time_attack, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=1,
                    ),
                ])

        if "Drift Attack" in self.challenge_sets:
            Empty = True

            if "Brand" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Score at least POINTS on DA with a car from the following brand: BRAND",
                        data={
                            "POINTS": (self.drift_attack_score_range, 1),
                            "DA": (self.base_drift_attack, 1),
                            "BRAND": (self.car_brands, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=1,
                    ),
                ])
                
            if "Class" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Score at least POINTS on DA with a car from the following class: CLASS",
                        data={
                            "POINTS": (self.drift_attack_score_range, 1),
                            "DA": (self.base_drift_attack, 1),
                            "CLASS": (self.car_classes, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=1,
                    ),
                ])

            if "Type" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Score at least POINTS on DA with a car from the following type: TYPE",
                        data={
                            "POINTS": (self.drift_attack_score_range, 1),
                            "DA": (self.base_drift_attack, 1),
                            "TYPE": (self.car_types, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=1,
                    ),
                ])

            if "Car" in self.condition_sets:
                Empty = False
                templates.extend([
                    GameObjectiveTemplate(
                        label="Score at least POINTS on DA with the following car: CAR",
                        data={
                            "POINTS": (self.drift_attack_score_range, 1),
                            "DA": (self.base_drift_attack, 1),
                            "CAR": (self.cars, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=1,
                    ),
                ])

            if Empty:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Score at least POINTS on DA",
                        data={
                            "POINTS": (self.drift_attack_score_range, 1),
                            "DA": (self.base_drift_attack, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=1,
                    ),
                ])

        if "EventLab" in self.challenge_sets: 
            templates.extend([
                GameObjectiveTemplate(
                    label="Play the EVENTLAB EventLab Blueprint on page PAGE of the TAB tab",
                    data={
                        "EVENTLAB": (self.eventlab, 1),
                        "PAGE": (self.eventlab_page_range, 1),
                        "TAB": (self.eventlab_tabs, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
            ])
        
        return templates
                
    @property
    def car_sets(self) -> List[str]:
        return sorted(self.archipelago_options.forza_horizon_6_car_set.value)   

    @property
    def challenge_sets(self) -> List[str]:
        return sorted(self.archipelago_options.forza_horizon_6_challenge_type.value)

    @property
    def condition_sets(self) -> List[str]:
        return sorted(self.archipelago_options.forza_horizon_6_condition_type.value)

    @property
    def my_car_list(self) -> List[str]:
        return sorted(self.archipelago_options.forza_horizon_6_car_list.value)

    @property
    def has_car_set_playlist_history(self) -> bool:
        return "Playlist History" in self.car_sets

    @property
    def has_car_set_playlist_welcome(self) -> bool:
        return "Playlist Welcome To Japan" in self.car_sets

    @property
    def has_car_set_playlist_decades(self) -> bool:
        return "Playlist Horizon Decades" in self.car_sets

    @property
    def has_car_set_playlist_exotics(self) -> bool:
        return "Playlist Italian Exotics" in self.car_sets
        
    @property
    def has_car_set_playlist_mascot(self) -> bool:
        return "Playlist Horizon Mascot Party" in self.car_sets
        
    @property
    def has_car_set_playlist_british(self) -> bool:
        return "Playlist British Automotive" in self.car_sets

    @property
    def has_car_set_wheelspin(self) -> bool:
        return "Wheelspin" in self.car_sets

    @property
    def has_car_set_car_pass(self) -> bool:
        return "Car Pass DLC" in self.car_sets

    @property
    def has_car_set_partnership(self) -> bool:
        return "Partnership DLC" in self.car_sets

    @property
    def has_car_set_preorder(self) -> bool:
        return "Preorder Bonus DLC" in self.car_sets

    @property
    def has_car_set_welcome_pack(self) -> bool:
        return "Welcome Pack DLC" in self.car_sets

    @property
    def has_car_set_vip(self) -> bool:
        return "VIP DLC" in self.car_sets

    @property
    def has_car_set_time_attack_car_pack(self) -> bool:
        return "Time Attack Car Pack DLC" in self.car_sets

    @property
    def has_car_set_italian_passion(self) -> bool:
        return "Italian Passion Car Pack DLC" in self.car_sets

    @property
    def include_car_challenges(self) -> bool:
        return bool(self.archipelago_options.forza_horizon_6_car_challenge.value)
        
    @property
    def include_only_car_challenges(self) -> bool:
        return bool(self.archipelago_options.forza_horizon_6_only_car_challenge.value)

    @property
    def include_job_challenges(self) -> bool:
        return bool(self.archipelago_options.forza_horizon_6_job_challenge.value)

    @property
    def include_gift_challenges(self) -> bool:
        return bool(self.archipelago_options.forza_horizon_6_gift_challenge.value)

    @property
    def include_cruise_challenges(self) -> bool:
        return bool(self.archipelago_options.forza_horizon_6_cruise_challenge.value)
        
    @property
    def include_mastery_challenges(self) -> bool:
        return bool(self.archipelago_options.forza_horizon_6_mastery_challenge.value)    

    @property
    def use_car_list(self) -> bool:
        return bool(self.archipelago_options.forza_horizon_6_use_car_list.value)

    @functools.cached_property
    def tracks_base_road(self) -> List[str]:
        return [
            "Shirakawa Circuit",
            "Daikoku Circuit",
            "Tokyo Railway Sprint",
            "Festival Sprint",
            "Shimanoyama Circuit",
            "Irokawa Circuit",
            "Narai-Juku Circuit",
            "Shikisai Sprint",
            "Venus Sprint",
            "Coastline Sprint",
            "Electric Town Circuit",
            "Satta Sprint",
            "Highway Circuit",
            "Ito Sprint",
            "Hokubu Circuit",
            "Shimanoyama Sprint",
            "Soni Circuit",
            "Legend Island Circuit",
            "Seaside Park Sprint",
            "Tateyama Kurobe Sprint",
            "Endamame Circuit",
        ]

    @functools.cached_property
    def tracks_base_dirt(self) -> List[str]:
        return [
            "Airfield Trail",
            "Taiyaki Scramble",
            "Sekibe Scramble",
            "Kinkaku-ji Trail",
            "Chiheisen Scramble",
            "Horizon Stadium Scramble",
            "Waterfall Trail",
            "Sotoyama Scramble",
            "Hirosaki Scramble",
            "Takashiro Trail",
            "Hokubu Trail",
            "Kawazu Nandaru Scramble",
            "Bamboo Forest Scramble",
            "Ine Scramble",
            "Sunflower Scramble",
            "Cherry Field Trail",
            "Oyashirazu Trail",
            "Ito Trail",
            "Nukabira Trail",
            "Legend Island Trail",
        ]

    @functools.cached_property
    def tracks_base_cross_country(self) -> List[str]:
        return [
            "Wind Farm Cross-Country",
            "Temple Cross-Country",
            "Stadium Cross-Country Circuit",
            "City Docks Cross-Country Circuit",
            "Shinjuku Gyoen Cross-Country",
            "Shimanoyama Cross-Country",
            "Oka Cross-Country Circuit",
            "Snow Forest Cross-Country Circuit",
            "Takashiro Cross-Country",
            "Soni Highlands Cross-Country",
            "Naruo Cross-Country Circuit",
            "Nangan Cross-Country Circuit",
            "Izu Cross-Country",
            "Yahikoyama Cross-Country",
            "Edogawa Cross-Country Circuit",
            "Ruriko-ji Cross-Country",
            "Tateyama Alpine Cross-Country",
            "Legend Island Cross-Country Circuit",
        ]

    @functools.cached_property
    def tracks_base_street(self) -> List[str]:
        return [
            "Rainbow Bridge Descent",
            "Daikoku Chase",
            "Tokyo City Docks Charge",
            "Minami Chase",
            "Matsumi Climb",
            "Shimanoyama Charge",
            "Festival Chase",
            "River Descent",
            "Cedar Run",
            "Kita Ine",
            "Sunflower Charge",
            "Nachi Run",
            "Hokubu Ascent",
            "Okishinaimura Run",
            "Norikura Descent",
        ]
    
    @functools.cached_property
    def tracks_base_touge(self) -> List[str]:
        return [
            "Hakone Nanamagari",
            "Arashiyama Takao",
            "Mt. Haruna",
            "Norikura Skyline",
            "Bandai Azuma",
        ]

    @functools.cached_property    
    def tracks_base_drag(self) -> List[str]:
        return [
            "Horizon Festival Drag Strip",
            "Irokawa Space Centre Drag Strip",
            "Ito Airfield Drag Strip",
        ]

    def tracks(self) -> List[str]:
        tracks: List[str] = sorted(
            self.tracks_base_road
            + self.tracks_base_dirt
            + self.tracks_base_cross_country
            + self.tracks_base_street
            + self.tracks_base_drag
        )
        
        return sorted(tracks)
    
    def tracks_touge(self) -> List[str]:
        tracks_touge: List[str] = self.tracks_base_touge[:]
        return sorted(tracks_touge)
        

    @functools.cached_property
    def tracks_long_base(self) -> List[str]:
        return [
            "The Goliath",
            "The Colossus",
            "The Gauntlet",
            "The Titan",
        ]

    def tracks_long(self) -> List[str]:
        tracks: List[str] = self.tracks_long_base[:]
        return sorted(tracks)

    def tracks_including_long(self) -> List[str]:
        return sorted(self.tracks() + self.tracks_long())

    @functools.cached_property
    def pr_stunts_base(self) -> List[str]:
        return [
            "Festival Leap Danger Sign",
            "Mt. Fuji View Danger Sign",
            "Rollercoaster Leap Danger Sign",
            "Stadium Jump Danger Sign",
            "Highway Jump Danger Sign",
            "Clifftop Crest Danger Sign",
            "Alpine Heights Danger Sign",
            "Highlands Danger Sign",
            "Circuit Leap Danger Sign",
            "Airfield Take-Off Danger Sign",
            "Seaside Heights Danger Sign",
            "Tanbo Launch Danger Sign",
            "Shirakawa-go Danger Sign",
            "Azure Drive Danger Sign",
            "Farmland Falls Danger Sign",
            "Irokawa Launch Danger Sign",
            "Nangan Heights Danger Sign",
            "Tokyo City Lookout Danger Sign",
            "Tokyo City Dockside Danger Sign",
            "Railway Bridge Danger Sign",
            "Bandai Azuma Skyline Drift Zone",
            "Inner City Run Drift Zone",
            "Kawazu Nandaru Loop Bridge Drift Zone",
            "Red Road Drift Zone",
            "Minamino Horseshoe Drift Zone",
            "Nukabira Turn Drift Zone",
            "Shiro Switch Drift Zone",
            "Thunderbird Drift Zone",
            "Cedar Grove Drift Zone",
            "Hakone Nanamagari Drift Zone",
            "Seaside Trail Drift Zone",
            "Shirakawa Curves Drift Zone",
            "Turbine Trail Drift Zone",
            "Mt. Haruna Drift Zone",
            "Hairpin Drift Zone",
            "River Run Drift Zone",
            "Kodachi Run Drift Zone",
            "Tokyo City Docks Drift Zone",
            "Sunflower Fields Drift Zone",
            "Meoto Iwa Turn Drift Zone",
            "River Split Speed Trap",
            "Lakeside Valley Speed Trap",
            "Rainbow Run Speed Trap",
            "Ito Straight Speed Trap",
            "Tokyo City Run-Up Speed Trap",
            "Festival Line Speed Trap",
            "Flower Run Speed Trap",
            "Crossover Speed Trap",
            "Hirosaki Castle Speed Trap",
            "Highland Road Speed Trap",
            "Takashiro Bridge Speed Trap",
            "Irabu Ohashi Bridge Speed Trap",
            "Shirakawa-go Straight Speed Trap",
            "Akihabara Straight Speed Trap",
            "Nangan Turn Speed Trap",
            "Lake Viewing Speed Trap",
            "Airfield Runway Speed Trap",
            "Ine Beach Speed Trap",
            "Bamboo Hilltop Speed Trap",
            "Crop Fields Speed Trap",
            "Daikoku Parking Area Speed Trap",
            "Jodogahama Grove Speed Trap",
            "Izu Skyline Speed Trap",
            "Stadium Back Road Speed Trap",
            "Main Street Speed Trap",
            "Riverside Speed Trap",
            "Cedar Woodland Speed Trap",
            "Shibuya Crossing Speed Trap",
            "Snowbank Speed Trap",
            "Island Road Speed Trap",
            "Highway View Speed Zone",
            "Festival Loop Speed Zone",
            "Pylons Speed Zone",
            "Yahikoyama Curve Speed Zone",
            "Fuji Shibazakura Speed Zone",
            "Mountain Pass Speed Zone",
            "Kōzokudō Speed Zone",
            "Temple Run-Up Speed Zone",
            "Snow Slopes Speed Zone",
            "Tateyama Kurobe Alpine Route Speed Zone",
            "Hirosaki Tangle Speed Zone",
            "Tea Farm Speed Zone",
            "Okishinaimura Speed Zone",
            "Yama Trail Speed Zone",
            "Farmland Curve Speed Zone",
            "Ocean Highway Speed Zone",
            "Seaside Park Speed Zone",
            "Hanado Speed Zone",
            "Arashiyama Run Speed Zone",
            "Minamino Curve Speed Zone",
            "Tall Trees Speed Zone",
            "Deep Forest Speed Zone",
            "Hakone Turns Speed Zone",
            "Matsumi Curve Speed Zone",
            "Airfield Grove Speed Zone",
            "Forest Straight Speed Zone",
            "City Sights Speed Zone",
            "Underground Tunnel Speed Zone",
            "Ine Backstreet Speed Zone",
            "Coastal Cliffside Speed Zone",
            "Bridge Underpasses Trailblazer",
            "Kodachi Descent Trailblazer",
            "Nachi Falls Trailblazer",
            "Mountain Descent Trailblazer",
            "Forest Cut-Through Trailblazer",
            "Coastal Descent Trailblazer",
            "Ropeway Run Trailblazer",
            "Kudarizaka Trailblazer",
            "On Par Trailblazer",
            "Sekibe Kaijo Trailblazer",
            "Horizon Kaido Trailblazer",
        ]

    def pr_stunts(self) -> List[str]:
        pr_stunts: List[str] = self.pr_stunts_base[:]
        return sorted(pr_stunts)

    @functools.cached_property
    def stories_base(self) -> List[str]:
        return [
            "Day Trip - Sotoyama",
            "Day Trip - Takashiro",
            "Day Trip - Ito",
            "Day Trip - Hokubu and Minamino",
            "Day Trip - North Shimanoyama",
            "Day Trip - South Shimanoyama",
            "Day Trip - Tokyo City",
            "Day Trip - Daikoku",
            "Day Trip - Nangan",
            "Drift Club Japan - Tokyo Drifters",
            "Drift Club Japan - Welcome to Drift Club",
            "Drift Club Japan - One Word: 'Touge'",
            "Drift Club Japan - Don't Look Down",
            "Drift Club Japan - Ready, Set...",
            "Drift Club Japan - Drift-zoku",
            "Moto Auto Zine - In Focus",
            "Moto Auto Zine - Shutter Speed",
            "Moto Auto Zine - Flying Shot",
            "Moto Auto Zine - Smoke and Tires",
            "Moto Auto Zine - Modern Tradition",
            "Moto Auto Zine - Shibuya Showstopper",
            "Yuji's Auto - Comfort and Speed",
            "Yuji's Auto - Flying Finish",
            "Yuji's Auto - Rush Hour",
            "Yuji's Auto - No Chill",
            "Yuji's Auto - Headline Act",
            "Yuji's Auto - To the Parade!",
        ]
        
    def stories(self) -> List[str]:
        stories: List[str] = self.stories_base[:]
        return sorted(stories)

    @functools.cached_property
    def car_brands_base(self) -> List[str]:
        return [
            "Abarth",
            "Acura",
            "Alfa Romeo",
            "Alumicraft",
            "AMG Transport Dynamics",
            "Apollo",
            "Ariel",
            "Aston Martin",
            "Audi",
            "Austin-Healey",
            "Autozam",
            "BAC",
            "Bentley",
            "BMW",
            "Buick",
            "Cadillac",
            "Can-Am",
            "Casey Currie Motorsports",
            "Chevrolet",
            "Datsun",
            "DeBerti",
            "DeLorean",
            "Dodge",
            "Ferrari",
            "Ford",
            "Formula Drift",
            "Funco Motorsports",
            "GMC",
            "Gordon Murray Automotive",
            "GR",
            "Hennessey",
            "Holden",
            "Honda",
            "HSV",
            "Hyundai",
            "Jaguar",
            "Jeep",
            "Jimco",
            "Koenigsegg",
            "KTM",
            "Lamborghini",
            "Lancia",
            "Land Rover",
            "Lexus",
            "Lincoln",
            "Lotus",
            "Lucid",
            "Maserati",
            "Mazda",
            "McLaren",
            "Mercedes-AMG",
            "Mercedes-Benz",
            "Meyers",
            "MG",
            "MINI",
            "Mitsubishi",
            "Nissan",
            "Noble",
            "Opel",
            "Pagani",
            "Peel",
            "Penhall",
            "Peugeot",
            "Playground",
            "Plymouth",
            "Polaris",
            "Pontiac",
            "Porsche",
            "Radical",
            "Ram",
            "Reliant",
            "Renault",
            "Rimac",
            "RIVIAN",
            "RJ Anderson",
            "Saleen",
            "Schuppan",
            "Shelby",
            "SIERRA Cars",
            "Subaru",
            "Toyota",
            "TVR",
            "Ultima",
            "Volkswagen",
            "Volvo",
            "Wuling",
            "Zenvo",
        ]

    def car_brands(self) -> List[str]:
        car_brands: List[str] = self.car_brands_base[:]
        return sorted(set(car_brands))

    @staticmethod
    def car_classes() -> List[str]:
        return [
            "R Class",
            "S2 Class",
            "S1 Class",
            "A Class",
            "B Class",
            "C Class",
            "D Class",
        ]

    @staticmethod
    def car_classes_alternate() -> List[str]:
        return [
            "an R Class",
            "an S2 Class",
            "an S1 Class",
            "an A Class",
            "a B Class",
            "a C Class",
            "a D Class",
        ]

    @staticmethod
    def car_types() -> List[str]:
        return [
            "Buggies",
            "Classic Muscle",
            "Classic Racers",
            "Classic Rally",
            "Classic Sports Cars",
            "Cult Cars",
            "Drift Cars",
            "Eclectic Domestics",
            "Extreme Track Toys",
            "GT Cars",
            "Hot Hatch",
            "Hypercars",
            "Modern Muscle",
            "Modern Rally",
            "Modern Sports Cars",
            "Modern Super Cars",
            "Modern Super Saloons",
            "Offroad",
            "Pickups & 4x4's",
            "Rally Monsters",
            "Rare Classics",
            "Retro Hot Hatch",
            "Retro Muscle",
            "Retro Racers",
            "Retro Rally",
            "Retro Sports Cars",
            "Retro Super Cars",
            "Retro Super Saloons",
            "Rods & Customs",
            "Sports Utility Heroes",
            "Super GT",
            "Super Hot Hatch",
            "Track Toys",
            "Unlimited Buggies",
            "Unlimited Offroad",
            "Utility Heroes",
            "UTV's",
            "Vintage Racers",
        ]

    @functools.cached_property
    def skills_standard(self) -> List[str]:
        return [
            "Air",
            "Great Air",
            "Awesome Air",
            "Ultimate Air",
            "Burnout",
            "Great Burnout",
            "Awesome Burnout",
            "Ultimate Burnout",
            "Wreckage",
            "Great Wreckage",
            "Awesome Wreckage",
            "Ultimate Wreckage",
            "Drift",
            "Great Drift",
            "Awesome Drift",
            "Ultimate Drift",
            "E-Drift",
            "Great E-Drift",
            "Awesome E-Drift",
            "Ultimate E-Drift",
            "J-Turn",
            "Great J-Turn",
            "Awesome J-Turn",
            "Ultimate J-Turn",
            "One-Eighty",
            "Great One-Eighty",
            "Awesome One-Eighty",
            "Ultimate One-Eighty",
            "Clean Racing",
            "Great Clean Racing",
            "Awesome Clean Racing",
            "Ultimate Clean Racing",
            "Drafting",
            "Great Drafting",
            "Awesome Drafting",
            "Ultimate Drafting",
            "Near Miss",
            "Great Near Miss",
            "Awesome Near Miss",
            "Ultimate Near Miss",
            "Pass",
            "Great Pass",
            "Awesome Pass",
            "Ultimate Pass",
            "Skill Chain",
            "Great Skill Chain",
            "Awesome Skill Chain",
            "Ultimate Skill Chain",
            "Speed",
            "Great Speed",
            "Awesome Speed",
            "Ultimate Speed",
        ]

    @functools.cached_property
    def skills_combo(self) -> List[str]:
        return [
            "Wrecking Ball",
            "Drift Tap",
            "Sideswipe",
            "Crash Landing",
            "Ebisu Style",
            "Kangaroo",
            "Airborne Pass",
            "Daredevil",
            "Hard Charger",
            "Lucky Escape",
            "Show Off",
            "Slingshot",
            "Stuntman",
            "Threading the Needle",
            "Triple Pass",
            "Clean Start",
        ]

    @functools.cached_property
    def skills_wreck(self) -> List[str]:
        return [
            "Abominable",
            "Bamboom!",
            "Bullion for You",
            "Clean Sweep",
            "Feat of Clay",
            "Feed Me!",
            "Landscaping",
            "Lumberjack",
            "Road Open",
            "Shredder",
            "Under The Sea",
            "Waterworks",
            "Wrong Number",
            "Drift Tap",
            "Two Wheels",
            "Barrel Roll",
            "Trading Paint",
        ]

    def skills(self) -> List[str]:
        skills: List[str] = sorted(
            self.skills_standard
            + self.skills_combo
            + self.skills_wreck
        )
        
        return sorted(skills)

    @staticmethod
    def drivatar_difficulties() -> List[str]:
        return [
            "TOURIST",
            "NEW RACER",
            "NOVICE",
            "AVERAGE",
            "ABOVE AVERAGE",
            "HIGHLY SKILLED",
            "EXPERT",
            "PRO",
            "UNBEATABLE",
        ]

    @staticmethod
    def race_placements() -> List[str]:
        return [
            "1st",
            "2nd or better",
            "3rd or better",
            "4th or better",
        ]

    @staticmethod
    def star_amount_range() -> range:
        return range(1, 4)

    @staticmethod
    def online_modes() -> List[str]:
        return [
            "Hide & Seek",
            "The Eliminator",
            "Horizon Racing",
            "Spec Racing",
            "Touge Showdown",
            "Horizon Drift",
        ]

    @staticmethod
    def eventlab() -> List[str]:
        return [
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "6th",
            "7th",
            "8th",
            "9th",
            "10th",
            "11th",
            "12th",
            "13th",
            "14th",
            "15th",
        ]

    @staticmethod
    def eventlab_page_range() -> range:
        return range(1, 6)

    @staticmethod
    def eventlab_tabs() -> List[str]:
        return [
            "Trending",
            "Featured",
            "Best of the Month",
        ]

    @staticmethod
    def opp_number() -> range:
        return range(4, 12)

    @staticmethod
    def lap_number() -> range:
        return range(1, 6)

    @staticmethod
    def weather() -> List[str]:
        return [
            "Clear",
            "Clear Post-Rain",
            "Cloudy",
            "Cloudy Post-Rain",
            "Overcast",
            "Light Precipitation",
            "Heavy Precipitation",
            "Gale",
            "Fog",
        ]

    @staticmethod
    def time() -> List[str]:
        return [
            "Dawn",
            "Sunrise",
            "Morning",
            "Early Afternoon",
            "Late Afternoon",
            "Sunset",
            "Evening",
            "Night",
        ]

    @staticmethod
    def traffic() -> List[str]:
        return [
            "Traffic ON",
            "Traffic OFF",
        ]

    @staticmethod
    def cameras() -> List[str]:
        return [
            "BUMPER",
            "BONNET",
            "COCKPIT",
            "DRIVER",
            "CHASE NEAR",
            "CHASE FAR",
        ]

    @staticmethod
    def assists() -> List[str]:
        return [
            "EASY",
            "MEDIUM",
            "HARD",
            "ULTIMATE",
        ]

    @staticmethod
    def assists_single() -> List[str]:
        return [
            "Turn Rewind off",
            "Set Damage & Tire Wear to Simulation",
            "Turn Driving Line off",
            "Set Shifting to Manual",
            "Set Shifting to Manual W/ Clutch",
            "Turn Stability Control off",
            "Turn Traction Control off",
            "Turn Anti-Lock off",
            "Set Steering to Simulation",
        ]
        
    @functools.cached_property
    def base_cars(self) -> List[str]:
        return [
            "1973 Mazda RX-3 Forza Edition",
            "1994 Mazda MX-5 Miata Forza Edition",
            "2022 Subaru BRZ Forza Edition",
            "1992 Alfa Romeo 155 Q4",
            "2014 Alfa Romeo 4C",
            "1964 Aston Martin DB5",
            "2019 Aston Martin Vantage",
            "1987 Buick Regal GNX",
            "1999 Dodge Viper GTS ACR",
            "2002 Ferrari Enzo Ferrari",
            "1965 Ford Mustang GT Coupe",
            "2009 Ford Focus RS",
            "1970 GMC Jimmy",
            "1986 Honda Civic Si",
            "2016 Koenigsegg Regera",
            "2020 Land Rover Defender 110 X",
            "2010 Lexus LFA",
            "2016 Mazda MX-5",
            "2018 McLaren 600LT Coupé",
            "1990 Mercedes-Benz 190 E 2.5-16 Evolution II",
            "2012 Mercedes-Benz C 63 AMG Coupé Black Series",
            "2001 Mitsubishi Lancer Evolution VI GSR TM Edition",
            "1987 Nissan Skyline GTS-R",
            "1989 Nissan Silvia K's",
            "1994 Nissan Fairlady Z Version S Twin Turbo",
            "2010 Pagani Zonda Cinque Roadster",
            "2024 Ram 1500 TRX",
            "2018 TVR Griffith",
            "1992 Toyota Celica GT-Four RC ST185",
            "2023 Toyota Camry TRD",
            "2554 AMG Transport Dynamics M12S Warthog CST",
            "1962 Ferrari 250 GT Berlinetta Lusso",
            "1987 Ferrari F40",
            "2017 Ford #14 Rahal Letterman Lanigan Racing Fiesta",
            "2017 Ford #25 'Brocky' Ultra4 Bronco RTR",
            "2017 Ford Focus RS",
            "2024 Ford Mustang Dark Horse",
            "1997 Formula Drift #777 Nissan 240SX",
            "2007 Formula Drift #117 599 GTB Fiorano",
            "2009 Formula Drift #99 Mazda RX-8",
            "2020 Gordon Murray Automotive T.50",
            "2005 Honda NSX-R",
            "1991 Jaguar Sport XJR-15",
            "2017 Koenigsegg Agera RS",
            "2019 Lamborghini Urus",
            "2024 Lamborghini Revuelto",
            "2015 Land Rover Range Rover Sport SVR",
            "1997 Maserati Ghibli Cup",
            "1992 Mazda RX-7 Type R",
            "2017 Mazda MX-5 Cup",
            "2013 Mercedes-Benz G 65 AMG",
            "2024 Nissan GT-R Nismo",
            "1984 Opel Manta 400",
            "2021 Polaris RZR Pro XP Ultimate",
            "1970 Porsche #3 917 LH",
            "2012 Porsche 911 GT3 RS 4.0",
            "2014 Porsche 918 Spyder",
            "2022 Porsche 718 Cayman GT4 RS",
            "2016 RJ Anderson #37 Polaris RZR Pro 2 Truck",
            "1997 Toyota Chaser 2.5 Tourer V",
            "1963 Volkswagen Type 2 De Luxe",
            "2016 Ariel Nomad",
            "2022 Aston Martin Valkyrie AMR Pro",
            "2019 BMW Z4 Roadster",
            "2021 Bentley Continental GT Convertible",
            "1969 Dodge Charger Daytona HEMI",
            "2018 Dodge Challenger SRT Demon",
            "1984 Honda City E II",
            "1991 Honda Beat",
            "1994 Honda Acty",
            "1994 Honda Prelude Si",
            "2023 Honda Civic Type R",
            "1986 MG Metro 6R4",
            "1997 Toyota Soarer 2.5 GT-T",
            "1998 Toyota Supra RZ",
            "2020 Toyota GR Supra",
            "1968 Abarth 595 esseesse",
            "1980 Abarth Fiat 131",
            "2001 Acura Integra Type R",
            "2002 Acura RSX Type S",
            "2023 Acura Integra A-Spec",
            "1965 Alfa Romeo Giulia Sprint GTA Stradale",
            "1968 Alfa Romeo 33 Stradale",
            "2007 Alfa Romeo 8C Competizione",
            "2017 Alfa Romeo Giulia Quadrifoglio",
            "2015 Alumicraft Class 10 Race Car",
            "2021 Alumicraft #122 Class 1 Buggy",
            "2022 Alumicraft #6165 Trick Truck",
            "2013 Ariel Atom 500 V8",
            "2017 Aston Martin DB11",
            "2017 Aston Martin Vulcan AMR Pro",
            "2023 Aston Martin Valkyrie",
            "1986 Audi #2 Audi Sport quattro S1",
            "2001 Audi RS 4 Avant",
            "2003 Audi RS 6",
            "2006 Audi RS 4",
            "2009 Audi R8 LMS",
            "2009 Audi RS 6",
            "2010 Audi TT RS Coupé",
            "2011 Audi RS 3 Sportback",
            "2011 Audi RS 5 Coupé",
            "2013 Audi RS 4 Avant",
            "2013 Audi RS 7 Sportback",
            "2015 Audi RS 6 Avant",
            "2015 Audi S1",
            "2016 Audi R8 V10 plus",
            "2018 Audi RS 4 Avant",
            "2020 Audi R8 V10 performance",
            "2020 Audi RS 3 Sedan",
            "2021 Audi RS 6 Avant",
            "2021 Audi RS 7 Sportback",
            "2021 Audi RS e-tron GT",
            "1965 Austin-Healey 3000 MkIII",
            "1993 Autozam AZ-1",
            "2014 BAC Mono",
            "1957 BMW Isetta 300 Export",
            "1973 BMW 2002 Turbo",
            "1988 BMW M3",
            "1988 BMW M5",
            "1995 BMW 850CSi",
            "1995 BMW M5",
            "1997 BMW M3",
            "2003 BMW M5",
            "2005 BMW M3",
            "2008 BMW M3",
            "2008 BMW Z4 M Coupé",
            "2009 BMW M5",
            "2010 BMW M3 GTS",
            "2011 BMW X5 M",
            "2012 BMW M5",
            "2014 BMW M4 Coupé",
            "2015 BMW i8",
            "2016 BMW M4 GTS",
            "2020 BMW M8 Competition Coupé",
            "2021 BMW M4 Competition Coupé",
            "2022 BMW M5 CS",
            "2022 BMW iX xDrive50",
            "2023 BMW M2",
            "2024 BMW X6 M Competition",
            "2013 Cadillac XTS Limousine",
            "2016 Cadillac ATS-V",
            "2016 Cadillac CTS-V Sedan",
            "2022 Cadillac CT4-V Blackwing",
            "2022 Cadillac CT5-V Blackwing",
            "2018 Can-Am Maverick X RS Turbo R",
            "1953 Chevrolet Corvette",
            "1955 Chevrolet 150 Utility Sedan",
            "1957 Chevrolet Bel Air",
            "1964 Chevrolet Impala Super Sport 409",
            "1969 Chevrolet Camaro Super Sport Coupe",
            "1969 Chevrolet Nova Super Sport 396",
            "1970 Chevrolet Camaro Z28",
            "1970 Chevrolet Chevelle Super Sport 454",
            "1970 Chevrolet Corvette ZR-1",
            "1970 Chevrolet El Camino Super Sport 454",
            "1972 Chevrolet K-10 Custom",
            "1979 Chevrolet Camaro Z28",
            "1988 Chevrolet Monte Carlo Super Sport",
            "1995 Chevrolet Corvette ZR-1",
            "1996 Chevrolet Impala Super Sport",
            "2002 Chevrolet Corvette Z06",
            "2009 Chevrolet Corvette ZR1",
            "2015 Chevrolet Camaro Z/28",
            "2015 Chevrolet Corvette Z06",
            "2017 Chevrolet Camaro ZL1",
            "2018 Chevrolet Camaro ZL1 1LE",
            "2020 Chevrolet Corvette Stingray Coupe",
            "2020 Chevrolet Silverado LT Trail Boss",
            "2023 Chevrolet Corvette Z06",
            "1970 Datsun 510",
            "2013 DeBerti Jeep Wrangler Unlimited",
            "2018 DeBerti Chevrolet Silverado 1500 Drift Truck",
            "2019 DeBerti Ford Super Duty F-250 Lariat 'Transformer'",
            "2019 DeBerti Toyota Tacoma TRD ‘The Performance Truck’",
            "1982 DeLorean DMC-12",
            "1970 Dodge Coronet Super Bee",
            "2008 Dodge Viper SRT-10 ACR",
            "2015 Dodge Challenger SRT Hellcat",
            "2015 Dodge Charger SRT Hellcat",
            "2022 Dodge Challenger SRT Super Stock",
            "1962 Ferrari 250 GTO",
            "1967 Ferrari #24 Ferrari Spa 330 P4",
            "1969 Ferrari Dino 246 GT",
            "1970 Ferrari 512 S",
            "1989 Ferrari F40 Competizione",
            "1995 Ferrari F50",
            "2005 Ferrari FXX",
            "2007 Ferrari 430 Scuderia",
            "2009 Ferrari 458 Italia",
            "2010 Ferrari 599XX",
            "2013 Ferrari 458 Speciale",
            "2013 Ferrari LaFerrari",
            "2014 Ferrari FXX K",
            "2015 Ferrari 488 GTB",
            "2015 Ferrari F12tdf",
            "2017 Ferrari 812 Superfast",
            "2017 Ferrari J50",
            "2018 Ferrari FXX-K Evo",
            "2018 Ferrari Portofino",
            "2019 Ferrari 488 Pista",
            "2019 Ferrari Monza SP2",
            "2020 Ferrari SF90 Stradale",
            "1932 Ford De Luxe Five-Window Coupe",
            "1966 Ford #2 GT40 Mk II",
            "1968 Ford Mustang GT 2+2 Fastback",
            "1969 Ford Mustang Boss 302",
            "1973 Ford Capri RS3100",
            "1973 Ford XB Falcon GT",
            "1977 Ford #5 Escort RS1800 MkII",
            "1986 Ford F-150 XLT Lariat",
            "1992 Ford Escort RS Cosworth",
            "1993 Ford Mustang SVT Cobra R",
            "1994 Ford Supervan 3",
            "1999 Ford Racing Puma",
            "2000 Ford Mustang SVT Cobra R",
            "2001 Ford #4 Ford Focus RS",
            "2003 Ford Focus RS",
            "2010 Ford Crown Victoria Police Interceptor",
            "2011 Ford Transit SuperSportVan",
            "2013 Ford Mustang Shelby GT500",
            "2014 Ford #11 Rockstar F-150 Trophy Truck",
            "2014 Ford FPV Limited Edition Pursuit Ute",
            "2016 Ford Mustang Shelby GT350R",
            "2017 Ford GT",
            "2018 Ford Mustang RTR Spec 5",
            "2020 Ford #2069 Ford Performance Bronco R",
            "2020 Ford Mustang Shelby GT500",
            "2020 Ford Super Duty F-450 DRW PLATINUM",
            "2022 Ford Bronco Raptor",
            "2022 Ford Focus ST",
            "2023 Ford F-150 Raptor R",
            "2023 Ford Fiesta ST",
            "2024 Ford Mustang GT",
            "1989 Formula Drift #98 BMW 325i",
            "1995 Formula Drift #34 Toyota Supra MkIV",
            "2013 Formula Drift #777 Chevrolet Corvette",
            "2016 Formula Drift #530 HSV Maloo GEN-F",
            "2019 Formula Drift #411 Toyota Corolla Hatchback",
            "2020 Formula Drift #151 Toyota GR Supra",
            "2020 Formula Drift #91 BMW M2",
            "2023 Formula Drift #64 Forsberg Racing Nissan Z",
            "1991 GMC Syclone",
            "1992 GMC Typhoon",
            "2022 GMC HUMMER EV Pickup",
            "2025 GR GT Prototype",
            "2014 HSV GEN-F GTS",
            "2014 HSV Limited Edition GEN-F GTS Maloo",
            "2019 Hennessey Ford F-150 VelociRaptor 6X6",
            "2021 Hennessey Venom F5",
            "1977 Holden Torana A9X",
            "1970 Honda S800",
            "1992 Honda NSX-R",
            "1997 Honda Civic Type R",
            "2003 Honda S2000",
            "2004 Honda Civic Type R",
            "2007 Honda Civic Type R",
            "2015 Honda Civic Type R",
            "2015 Honda Ridgeline Baja Trophy Truck",
            "2018 Honda Civic Type R",
            "2022 Honda e",
            "2019 Hyundai Veloster N",
            "2020 Hyundai i30 N",
            "2021 Hyundai i20 N",
            "2022 Hyundai N Vision 74",
            "2023 Hyundai IONIQ 5 N",
            "1956 Jaguar D-Type",
            "1964 Jaguar Lightweight E-Type",
            "1993 Jaguar XJ220",
            "1993 Jaguar XJ220S TWR",
            "2010 Jaguar C-X75",
            "2012 Jeep Wrangler Rubicon",
            "2016 Jeep Trailcat",
            "2018 Jeep Grand Cherokee Trackhawk",
            "2020 Jeep JT",
            "2019 Jimco #240 Fastball Racing Class 6100 Spec Trophy Truck",
            "2020 Jimco #179 Hammerhead Class 1",
            "2018 KTM X-Bow GT4",
            "2008 Koenigsegg CCGT",
            "2011 Koenigsegg Agera",
            "2020 Koenigsegg Jesko",
            "1967 Lamborghini Miura P400",
            "2010 Lamborghini Murciélago LP 670-4 SV",
            "2012 Lamborghini Gallardo LP570-4 Spyder Performante",
            "2013 Lamborghini Veneno",
            "2018 Lamborghini Aventador SVJ",
            "2020 Lamborghini Essenza SCV12",
            "2020 Lamborghini Huracán STO",
            "2020 Lamborghini Sián Roadster",
            "2021 Lamborghini Countach LPI 800-4",
            "2022 Lamborghini Huracán Tecnica",
            "1986 Lancia Delta S4",
            "1992 Lancia Delta HF Integrale EVO",
            "2015 Lexus RC F",
            "2021 Lexus LC 500",
            "1997 Lotus Elise GT1",
            "1999 Lotus Elise Series 1 Sport 190",
            "2020 Lotus Evija",
            "2024 Lucid Air Sapphire",
            "1965 MINI Cooper S",
            "2012 MINI John Cooper Works GP",
            "2013 MINI X-Raid All4 Racing Countryman",
            "2008 Maserati MC12 Versione Corsa",
            "2022 Maserati MC20",
            "1973 Mazda RX-3",
            "1990 Mazda Savanna RX-7",
            "1994 Mazda MX-5 Miata",
            "2005 Mazda Mazdaspeed MX-5",
            "2010 Mazda Mazdaspeed 3",
            "2011 Mazda RX-8 R3",
            "2013 Mazda MX-5",
            "2022 Mazda MX-5 Miata RF",
            "1993 McLaren F1",
            "1997 McLaren F1 GT",
            "2011 McLaren 12C Coupé",
            "2013 McLaren P1",
            "2014 McLaren 650S Spider",
            "2015 McLaren 570S Coupé",
            "2019 McLaren Speedtail",
            "2021 McLaren 765LT Coupé",
            "2023 McLaren Artura",
            "2015 Mercedes-AMG GT S",
            "2016 Mercedes-AMG C 63 S Coupé",
            "2018 Mercedes-AMG E 63 S",
            "2020 Mercedes-AMG GT Black Series",
            "2020 Mercedes-AMG SLC 43 Final Edition",
            "2021 Mercedes-AMG Mercedes-AMG ONE",
            "2021 Mercedes-AMG SL 63",
            "1954 Mercedes-Benz 300 SL Coupé",
            "1955 Mercedes-Benz 300 SLR",
            "1987 Mercedes-Benz AMG Hammer Coupe",
            "2009 Mercedes-Benz SL 65 AMG Black Series",
            "2013 Mercedes-Benz A 45 AMG",
            "2014 Mercedes-Benz Unimog U5023",
            "2018 Mercedes-Benz X-Class",
            "1971 Meyers Manx",
            "2023 Meyers Manx 2.0",
            "1992 Mitsubishi Galant VR-4",
            "1995 Mitsubishi Eclipse GSX",
            "1995 Mitsubishi Montero Exceed 2800 TD",
            "1997 Mitsubishi GTO",
            "2004 Mitsubishi Lancer Evolution VIII MR",
            "2008 Mitsubishi Lancer Evolution X GSR",
            "1969 Nissan Fairlady Z 432",
            "1973 Nissan Skyline H/T 2000GT-R",
            "1989 Nissan S-Cargo",
            "1990 Nissan Pulsar GTI-R",
            "1992 Nissan Skyline GT-R",
            "1994 Nissan Silvia K's",
            "1995 Nissan Gloria Gran Turismo",
            "1995 Nissan NISMO GT-R LM",
            "1997 Nissan Stagea RS Four V",
            "1998 Nissan Silvia K's Aero",
            "2000 Nissan Skyline GT-R V Spec II",
            "2002 Nissan Silvia Spec-R",
            "2003 Nissan Fairlady Z",
            "2012 Nissan GT-R Black Edition (R35)",
            "2017 Nissan GT-R (R35)",
            "2019 Nissan 370Z Nismo",
            "2020 Nissan GT-R NISMO (R35)",
            "2024 Nissan Z NISMO",
            "2010 Noble M600",
            "2009 Pagani Zonda R",
            "2016 Pagani Huayra BC Coupe",
            "1962 Peel P50",
            "2011 Penhall The Cholla",
            "1991 Peugeot 205 Rallye",
            "1958 Plymouth Fury",
            "1968 Plymouth Barracuda Formula S",
            "1971 Plymouth Cuda 426 HEMI",
            "2021 Polaris RZR Pro XP Factory Racing Limited Edition",
            "1977 Pontiac Firebird Trans Am",
            "1987 Pontiac Firebird Trans Am GTA",
            "1973 Porsche 911 Carrera RS",
            "1985 Porsche #185 959 Prodrive Rally Raid",
            "1989 Porsche 944 Turbo",
            "1993 Porsche 928 GTS",
            "1993 Porsche 968 Turbo S",
            "1997 Porsche 911 GT1 Strassenversion",
            "2004 Porsche 911 GT3",
            "2005 Porsche Cayman GT3 WTAC",
            "2018 Porsche 718 Cayman GTS",
            "2018 Porsche 911 GT2 RS",
            "2018 Porsche Cayenne Turbo",
            "2018 Porsche Macan LPR Rally Raid",
            "2019 Porsche #70 Porsche Motorsport 935",
            "2019 Porsche 911 Carrera S",
            "2020 Porsche Taycan Turbo S",
            "2021 Porsche 911 GT3",
            "2021 Porsche Mission R",
            "2023 Porsche 911 GT3 RS",
            "2023 Porsche 911 Turbo S",
            "2015 Radical RXC Turbo",
            "1972 Reliant Supervan III",
            "1980 Renault 5 Turbo",
            "1993 Renault Clio Williams",
            "2008 Renault Mégane R26.R",
            "2010 Renault Megane RS 250",
            "2018 Renault Megane R.S.",
            "2022 Rivian R1T",
            "2020 SIERRA Cars #23 Yokohama ALPHA",
            "2021 SIERRA Cars 700R",
            "2021 SIERRA Cars RX3",
            "1965 Shelby Cobra Daytona Coupe",
            "1980 Subaru BRAT GL",
            "1990 Subaru LEGACY RS",
            "1994 Subaru Vivio RX-R",
            "1996 Subaru SVX",
            "1998 Subaru Impreza 22B-STi Version",
            "2004 Subaru IMPREZA WRX STI",
            "2005 Subaru IMPREZA WRX STI",
            "2005 Subaru LEGACY B4 2.0 GT",
            "2008 Subaru IMPREZA WRX STI",
            "2011 Subaru WRX STI",
            "2013 Subaru BRZ",
            "2015 Subaru WRX STI",
            "2022 Subaru BRZ",
            "2022 Subaru WRX",
            "2005 TVR Sagaris",
            "1979 Toyota FJ40",
            "1985 Toyota Sprinter Trueno GT Apex",
            "1991 Toyota Chaser GT Twin Turbo",
            "1991 Toyota Sera",
            "1992 Toyota Supra 2.0 GT",
            "1993 Toyota #1 T100 Baja Truck",
            "1994 Toyota Celica GT-Four ST205",
            "1995 Toyota MR2 GT",
            "2003 Toyota Celica Sport Specialty II",
            "2005 Toyota Crown Super Deluxe Taxi",
            "2013 Toyota 86",
            "2017 Toyota JPN Taxi",
            "2019 Toyota 4Runner TRD Pro",
            "2019 Toyota Tacoma TRD Pro",
            "2021 Toyota GR Yaris",
            "2022 Toyota GR86",
            "2025 Toyota Land Cruiser",
            "2015 Ultima Evolution Coupe 1020",
            "1963 Volkswagen Beetle",
            "1969 Volkswagen Class 5/1600 Baja Bug",
            "1982 Volkswagen Pickup LX",
            "1983 Volkswagen Golf GTI",
            "1992 Volkswagen Golf Gti 16v Mk2",
            "1995 Volkswagen Corrado VR6",
            "2010 Volkswagen Golf R",
            "2011 Volkswagen Scirocco R",
            "2014 Volkswagen Golf R",
            "2017 Volkswagen #34 Andretti Rally Cross Beetle",
            "2021 Volkswagen Golf R",
            "2022 Volkswagen Golf R",
            "1983 Volvo 242 Turbo Evolution",
            "2013 Wuling Sunshine S",
            "2022 Wuling Hongguang Mini EV",
            "2019 Zenvo TSR-S",
            "2016 Aston Martin Vulcan",
            "2024 Chevrolet Corvette E-Ray",
            "2014 Lamborghini Huracán LP 610-4",
            "2016 Lamborghini Centenario LP 770-4",
            "2013 SRT Viper GTS",
            "1990 Jaguar XJ-S",
        ]
        
    @functools.cached_property
    def wristband_cars(self) -> List[str]:
        return [
            "2023 Porsche 911 Rallye",
            "2020 BMW M2 Competition Coupé",
            "2022 Lamborghini Aventador LP 780-4 Ultimae",
            "2018 Subaru WRX STI ARX Supercar",
            "2022 Acura NSX Type S",
            "2007 Peugeot 207 Super 2000",
            "1985 Ford RS200 Evolution",
        ]
        
    @functools.cached_property
    def collection_cars(self) -> List[str]:
        return [
            "1981 BMW M1",
            "1969 Dodge Charger R/T",
            "1987 Ford Sierra Cosworth RS500",
            "2005 Ford GT",
            "2005 Honda NSX-R GT",
            "1997 Lamborghini Diablo SV",
            "1974 Lancia Stratos HF Stradale",
            "1962 Lincoln Continental",
            "1985 Mazda RX-7 GSL-SE",
            "1991 Mazda #55 Mazda 787B",
            "1995 Mitsubishi Lancer Evolution III GSR",
            "1997 Mitsubishi Montero Evolution",
            "2005 Mitsubishi #1 Sierra Sierra Enterprises Lancer Evolution Time Attack",
            "1971 Nissan Skyline 2000GT-R",
            "1983 Nissan #11 Tomica Skyline Turbo Super Silhouette",
            "1985 Nissan Safari Turbo",
            "1989 Nissan PAO",
            "1991 Nissan Figaro",
            "1998 Nissan #23 Pennzoil NISMO Skyline GT-R",
            "1998 Nissan R390 (GT1)",
            "1984 Peugeot 205 Turbo 16",
            "1982 Porsche 911 Turbo 3.3",
            "1987 Porsche 959",
            "1969 Toyota 2000GT",
            "1965 Alfa Romeo Giulia TZ2",
            "2013 Audi R8 Coupé V10 plus 5.2 FSI quattro",
            "2023 BMW M2 Forza Edition",
            "1967 Chevrolet Corvette Stingray 427",
            "2021 Dodge Durango SRT Hellcat",
            "1996 Ferrari F50 GT",
            "2022 Ford Supervan 4",
            "2018 Funco Motorsports F9",
            "1974 Honda Civic RS",
            "1984 Honda Civic CRX Mugen",
            "2022 Lamborghini Huracán Sterrato",
            "2010 Lexus LFA Forza Edition",
            "2018 Lotus Scura Motorsports Exige WTAC",
            "2018 MINI X-raid John Cooper Works Buggy",
            "2003 Porsche Carrera GT",
            "1965 Shelby Cobra 427 S/C",
            "1994 Subaru Vivio RX-R Forza Edition",
            "1985 Toyota Sprinter Trueno GT Apex Forza Edition",
            "2013 Toyota 86 Stories",
            "1965 Toyota Sports 800",
            "1990 Jaguar XJ-S Forza Edition",
        ]
    
    @functools.cached_property
    def playlist_history_cars(self) -> List[str]:
        return [
            "1972 Mazda Cosmo 110S Series II",
        ]
    
    @functools.cached_property
    def playlist_welcome_to_japan_cars(self) -> List[str]:
        return [
            # Series
            "2008 Mazda Furai",
            "2010 Nissan 370Z",
            
            # Summer
            "1999 Toyota Altezza RS200 Z EDITION",
            "2006 Mitsubishi Lancer Evolution IX MR",
            
            # Autumn
            "1997 Nissan Skyline GT-R V-Spec",
            "1991 Honda CR-X SiR",
            
            # Winter
            "2019 Subaru STI S209",
            "2016 Toyota Land Cruiser Arctic Trucks AT37",
            
            # Spring
            "1996 Toyota Starlet Glanza V",
            "1974 Toyota Corolla SR5",
            
            # Exclusive Reward
        ]
    
    @functools.cached_property
    def playlist_horizon_decades_cars(self) -> List[str]:
        return [
            # Series
            "1993 Porsche 911 Turbo S Leichtbau",
            "2018 Lotus Exige Cup 430",
            
            # Summer
            "1989 Volkswagen Rallye Golf",
            "1988 Lamborghini Countach LP5000 QV",
            
            # Autumn
            "1998 TVR Cerbera Speed 12",
            "1993 Schuppan 962CR",
            
            # Winter
            "2006 Dodge Ram SRT-10",
            "2003 Ford F-150 SVT Lightning",
            
            # Spring
            "2017 Mercedes-AMG GT R",
            "2017 Saleen S7 LM",
            
            # Exclusive Reward
        ]
    
    @functools.cached_property
    def playlist_italian_exotics_cars(self) -> List[str]:
        return [
            # Series
            "2024 Lamborghini Temerario",
            "2022 Ferrari 296 GTB",
            
            # Summer
            "1984 De Tomaso Pantera GT5",
            "2004 Maserati MC12",
            
            # Autumn
            "2017 Abarth 124 Spider",
            "2020 Lamborghini Huracán EVO",
            
            # Winter
            "1982 Lancia 037 Stradale",
            "2020 Ferrari Roma",
            
            # Spring
            "2022 Lamborghini Huracán EVO Spyder",
            "2021 Pagani Huayra R",
            
            # Exclusive Reward
        ]
    
    @functools.cached_property
    def playlist_horizon_mascot_party_cars(self) -> List[str]:
        return [
            # Series
            "1970 Honda N600",
            "1967 Renault 8 Gordini",
            
            # Summer
            "2018 Exomotive V8 XP-5",
            "1969 Datsun 2000 Roadster",
            
            # Autumn
            "2024 Chevrolet Camaro ZL1",
            "2016 Abarth 695 Biposto",
            
            # Winter
            "1974 Toyota Celica GT",
            "1989 Toyota MR2 SC",
            
            # Spring
            "1988 Mitsubishi Starion ESI-R",
            "1968 Dodge Dart HEMI Super Stock",
            
            # Exclusive Reward
        ]
    
    @functools.cached_property
    def playlist_british_automotive_cars(self) -> List[str]:
        return [
            # Series
            "2025 Bentley Continental GT Speed",
            "2019 Aston Martin Valhalla Concept Car",
            
            # Summer
            "2019 Ginetta G40 Junior",
            "2021 McLaren 620R",
            
            # Autumn
            "2015 Jaguar XKR-S GT",
            "2021 MINI John Cooper Works GP",
            
            # Winter
            "2006 Vauxhall Astra VXR",
            "2016 Bentley Bentayga",
            
            # Spring
            "2002 Lotus Esprit V8",
            "2023 Lotus Emira",
            
            # Exclusive Reward
        ]
    
    @functools.cached_property
    def wheelspin_cars(self) -> List[str]:
        return [
            "2019 Apollo Intensa Emozione",
            "2019 Aston Martin DBS Superleggera",
            "2019 Aston Martin Valhalla Concept Car",
            "1984 Audi Sport quattro",
            "2020 BMW M2 Competition Coupé",
            "2016 Bentley Bentayga",
            "2019 Casey Currie Motorsports #4402 Ultra 4 'Trophy Jeep'",
            "1960 Chevrolet Corvette",
            "2019 Chevrolet Corvette ZR1",
            "1968 Dodge Dart HEMI Super Stock",
            "1970 Dodge Challenger R/T",
            "2016 Dodge Viper ACR",
            "1984 Ferrari 288 GTO",
            "1992 Ferrari 512 TR",
            "1994 Ferrari F355 Berlinetta",
            "2012 Ferrari 599XX Evolution",
            "2019 Ferrari F8 Tributo",
            "1968 Ford Mustang GT 2+2 Fastback Forza Edition",
            "1986 Ford F-150 XLT Lariat Forza Edition",
            "2014 Ford Ranger T6 Rally Raid",
            "2017 Ford M-Sport Fiesta RS",
            "2020 Ford Super Duty F-450 DRW PLATINUM Forza Edition",
            "2022 Ford F-150 Lightning",
            "2006 Formula Drift #43 Dodge Viper SRT-10 ACR",
            "2015 Formula Drift #13 Ford Mustang",
            "2012 Hennessey Venom GT",
            "1961 Jaguar E-type",
            "2015 Koenigsegg One:1",
            "1999 Lamborghini Diablo GTR",
            "2011 Lamborghini Sesto Elemento",
            "2012 Lamborghini Aventador LP700-4",
            "2021 McLaren 620R",
            "2018 Mercedes-AMG GT 4-Door Coupé",
            "1990 Mercedes-Benz 190 E 2.5-16 Evolution II Forza Edition",
            "1998 Mercedes-Benz AMG CLK GTR",
            "2014 Mercedes-Benz G 63 AMG 6x6",
            "1989 Nissan S-Cargo Forza Edition",
            "1993 Nissan 240SX",
            "2012 Nissan GT-R Black Edition (R35) Forza Edition",
            "1970 Porsche #3 917 LH Forza Edition",
            "1995 Porsche 911 GT2",
            "2019 Porsche 911 GT3 RS",
            "2021 RJ Anderson #37 Polaris RZR Pro 4 Truck",
            "2021 Rimac Nevera",
            "2013 Wuling Sunshine S Forza Edition",
        ]
        
    @functools.cached_property
    def car_pass_cars(self) -> List[str]:
        return [
            "2003 Aston Martin DB7 GT",
            "2023 Audi R8 Coupé V10 GT RWD",
            "1972 Datsun #269 Attacking the Clock Racing 240Z 'All Carbon Hill Climb Beast'",
            "1972 Honda Z GT",
            "2008 Honda Civic Type R (FD2)",
            "2024 Koenigsegg Gemera",
            "1974 Mazda #123 Mad Mike 808 Wagon 'FURSTY'",
            "1972 Nissan Patrol",
            "1990 Nissan #12 Skyline GT-R (BNR32 Gr.A) JTC",
            "1998 Nissan Skyline GT-R 40th Anniversary",
            "2023 Toyota GR Corolla",
            "2024 Toyota Prius Prime XSE Premium",
            "1968 Alfa Romeo Autodelta Tipo 33/2 Daytona",
            "1957 Ford Thunderbird",
            "1983 Nissan Skyline 2000 Turbo RS",
            "1987 Porsche #203 Porsche AG 961",
            "2025 McLaren W1",
            "2023 Dodge Challenger SRT Demon 170",
            "1998 Renault Sport Spider",
            "1987 Porsche 911 Carrera Coupe ‘Luftauto 002’ ",
        ]
        
    @functools.cached_property
    def italian_passion_cars(self) -> List[str]:
        return [
            "2021 Alfa Romeo Giulia GTAm",
            "1990 Alfa Romeo SE 048SP",
            "1967 Ferrari 275 GTB4 Spider",
            "2025 Ferrari F80",
        ]
        
    @functools.cached_property
    def partnership_cars(self) -> List[str]:
        return [
            "1962 Peel P50 Trolli Edition",
            "1965 Toyota Sports 800 Fanta Edition",
        ]
        
    @functools.cached_property
    def preorder_cars(self) -> List[str]:
        return [
            "2017 Ferrari J50 Preorder Car",
        ]
        
    @functools.cached_property
    def time_attack_cars(self) -> List[str]:
        return [
            "1990 Honda #19 101 Motorsport CRX WTAC",
            "1992 Honda #21 Hardrace/JDMYard Civic WTAC",
            "2001 Honda #33 Integra WTAC",
            "2004 Honda #52 Evasive Motorsports S2000 WTAC",
            "1990 Mitsubishi #269 Attacking the Clock Racing Minicab Time Attack",
            "1993 Nissan #32 Skyline WTAC 'Xtreme GTR'",
            "2000 Nissan #36 Dream Project S15 Silvia WTAC",
            "1995 Toyota J&J Motorsport Supra WTAC",
        ]
        
    @functools.cached_property
    def vip_cars(self) -> List[str]:
        return [
            "1999 Dodge Viper GTS ACR Forza Edition",
            "2020 Lotus Evija Forza Edition",
            "2019 Toyota Tacoma TRD Pro Forza Edition",
        ]
        
    @functools.cached_property
    def welcome_cars(self) -> List[str]:
        return [
            "2021 BMW M4 Competition Coupé Welcome Pack",
            "2018 Ferrari FXX-K Evo Welcome Pack",
            "2023 Ford F-150 Raptor R Welcome Pack",
            "2020 Mercedes-AMG GT Black Series Welcome Pack",
            "2004 Mitsubishi Lancer Evolution VIII MR Welcome Pack",
        ]
        
    def cars(self) -> List[str]:
        if self.use_car_list:
            return self.my_car_list
        else:
            cars: List[str] = self.base_cars[:]
            cars.extend(sorted(self.collection_cars))
            cars.extend(sorted(self.wristband_cars))
            
            if self.has_car_set_playlist_history:
                cars.extend(self.playlist_history_cars)
            
            if self.has_car_set_playlist_welcome:
                cars.extend(self.playlist_welcome_to_japan_cars)
            
            if self.has_car_set_playlist_decades:
                cars.extend(self.playlist_horizon_decades_cars)
            
            if self.has_car_set_playlist_exotics:
                cars.extend(self.playlist_italian_exotics_cars)
            
            if self.has_car_set_playlist_mascot:
                cars.extend(self.playlist_horizon_mascot_party_cars)
            
            if self.has_car_set_playlist_british:
                cars.extend(self.playlist_british_automotive_cars)
            
            if self.has_car_set_wheelspin:
                cars.extend(self.wheelspin_cars)
            
            if self.has_car_set_car_pass:
                cars.extend(self.car_pass_cars)
                
            if self.has_car_set_partnership:
                cars.extend(self.partnership_cars)
            
            if self.has_car_set_preorder:
                cars.extend(self.preorder_cars)
            
            if self.has_car_set_welcome_pack:
                cars.extend(self.welcome_cars)
            
            if self.has_car_set_vip:
                cars.extend(self.vip_cars)
            
            if self.has_car_set_time_attack_car_pack:
                cars.extend(self.time_attack_cars)
            
            if self.has_car_set_italian_passion:
                cars.extend(self.italian_passion_cars)
            
            return sorted(cars)
      
    @functools.cached_property
    def base_time_attack(self) -> List[str]:
        return [
            "Legend Island Time Attack",
            "Sekibe Time Attack",
            "Hokubu Time Attack",
            "Soni Time Attack",
        ]
    
    @functools.cached_property
    def base_drift_attack(self) -> List[str]:
        return [
            "Shimanoyama Drift Attack",
        ]
      
    @functools.cached_property
    def base_car_meet(self) -> List[str]:
        return [
            "Okuibuki Car Meet",
            "Horizon Festival Car Meet",
            "Daikoku Parking Area Car Meet",
        ]
      
    @functools.cached_property
    def base_house(self) -> List[str]:
        return [
            "Tokyo House",
            "Soko 78",
            "Vision House",
            "Mei's House",
            "Fuji Unkai House",
            "Minka House",
            "Yashiki House",
            "Hakusan Mountain Lodge",
        ]
      
    @functools.cached_property
    def base_barn(self) -> List[str]:
        return [
            "Nissan Skyline 2000GT-R Barn",
            "Ford Sierra Coswoth RS500 Barn",
            "Porsche 911 Tubo 3.3 Barn",
            "Nissan R390 (GT1) Barn",
            "Honda NSX-R GT Barn",
            "Mitsubishi Montero Evolution Barn",
            "Lamborghini Diablo SV Barn",
            "Nissan #11 Tomica Skyline Turbo Super Silhouette Barn",
            "Nissan PAO Barn",
            "Mitsubishi #1 Sierra Sierra Time Attack Barn",
            "Peugeot 205 Turbo 16 Barn",
            "Toyota 2000GT Barn",
            "Lincoln Continental Barn",
            "Nissan #23 Pennzoil NISMO Skyline GT-R Barn",
            "Mazda #55 Mazda 787B Barn",
        ]
      
    @functools.cached_property
    def base_treasure(self) -> List[str]:
        return [
            "Lancia Stratos Treasure",
            "Mit. Evo III '95 Treasure",
            "BMW M1 Treasure",
            "Nissan Safari Treasure",
            "Porsche 959 Treasure",
            "Mazda RX-7 '85 Treasure",
            "Dodge Charger 69 Treasure",
            "Figaro '91 Treasure",
            "Ford GT '05 Treasure",
        ]
      
    @functools.cached_property
    def base_job(self) -> List[str]:
        return [
            "Tokyo City Food Delivery",
        ]
      
    @functools.cached_property
    def base_festival(self) -> List[str]:
        return [
            "Horizon Festival Site",
            "Legend Island Festival Site",
        ]
        
    @functools.cached_property
    def base_drag_meet(self) -> List[str]:
        return [
            "Festival Kilometer Drag Meet",
            "Irokawa Quarter Mile Drag Meet",
            "Ito Half-Mile Drag Meet",
        ]
        
    def locations(self) -> List[str]:
        locations: List[str] = sorted(
            self.base_festival
            + self.base_job
            + self.base_treasure
            + self.base_barn
            + self.base_house
            + self.base_car_meet
            + self.base_time_attack
            + self.base_drift_attack
            + self.base_drag_meet
            + self.tracks_including_long()
            + self.stories()
        )
        
        return sorted(locations)
        
    def time_attack(self) -> List[str]:
        time_attack: List[str] = self.base_time_attack[:]
        return sorted(time_attack)
        
    @staticmethod
    def time_attack_lap_range() -> range:
        return range(1, 11)
    
    @staticmethod
    def drift_attack_score_range() -> range:
        return range(20000, 150000, 5000)

    @staticmethod
    def star_amount_job_range() -> range:
        return range(1, 10)
        
# Archipelago Options
class ForzaHorizon6IncludeChallengeType(OptionSet):
    """
    Indicates which type of challenge should be included.
    
    - Single Race  : Finish 1 race in a position randomized between 1st and 4th
    - Triple Race  : Finish 3 races in a position randomized between 1st and 4th
    - Custom Race  : Finish 1 race with custom rules in a position randomized between 1st and 4th
    - Rival        : Complete a clean Rival time
    - PR Stunt     : Complete 3 or 5 PR Stunts
    - Skill        : Complete 3 or 5 Skills
    - Car Mastery  : Complete a Mastery Tree
    - Gift         : Gift a car
    - Online Round : Play a round of an online gamemode
    - Cruise       : Drive from a location A to a location B
    - Job          : Complete a full job shift
    - Story        : Complete a story
    - Time Attack  : Complete laps in Time Attack
    - Drift Attack : Complete a lap with randomized score in Drift Attack
    - EventLab     : Complete an EventLab event
    """
    display_name = "Forza Horizon 6 Challenge Type"
    valid_keys = {
        "Single Race",
        "Triple Race",
        "Custom Race",
        "Rival",
        "PR Stunt",
        "Skill",
        "Car Mastery",
        "Gift",
        "Online Round",
        "Cruise",
        "Job",
        "Story",
        "Time Attack",
        "Drift Attack",
        "EventLab"
    }

    default = valid_keys

class ForzaHorizon6IncludeConditionType(OptionSet):
    """Indicates which type of condition should be included"""
    display_name = "Forza Horizon 6 Challenge Type"
    valid_keys = {
        "Brand",
        "Class",
        "Type",
        "Car"
    }

    default = valid_keys
    
class ForzaHorizon6IncludeCarSet(OptionSet):
    """Indicates which pack of cars (Time-Gated exclusive, Wheelspin or DLC) can be required for car challenges"""
    display_name = "Forza Horizon 6 Car Sets"
    valid_keys = {
        "Playlist History",
        "Playlist Welcome To Japan",
        "Playlist Horizon Decades",
        "Playlist Italian Exotics",
        "Playlist Horizon Mascot Party",
        "Playlist British Automotive",
        "Wheelspin",
        "Car Pass DLC",
        "Partnership DLC",
        "Preorder Bonus DLC",
        "Welcome Pack DLC",
        "VIP DLC",
        "Time Attack Car Pack DLC",
        "Italian Passion Car Pack DLC"
    }

    default = valid_keys

class ForzaHorizon6IncludeMyCarList(Toggle):
    """Indicates whether to use your car list for car conditions"""
    display_name = "Forza Horizon 6 Include My Car List"

class ForzaHorizon6MyCarList(OptionSet):
    """
    Car list to use.
    
    Only relevant if "Forza Horizon 6 Include My Car List" is selected
    """
    display_name = "Forza Horizon 6 My Car List"
    default = []

