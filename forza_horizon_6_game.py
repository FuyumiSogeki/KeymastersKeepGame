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

        if "Championship Race" in self.challenge_sets:
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
            "1973 Mazda RX-3 Forza Edition (B Class)",
            "1994 Mazda MX-5 Miata Forza Edition (S2 Class)",
            "2022 Subaru BRZ Forza Edition (A Class)",
            "1992 Alfa Romeo 155 Q4 (C Class)",
            "2014 Alfa Romeo 4C (A Class)",
            "1964 Aston Martin DB5 (C Class)",
            "2019 Aston Martin Vantage (A Class)",
            "1987 Buick Regal GNX (C Class)",
            "1999 Dodge Viper GTS ACR (B Class)",
            "2002 Ferrari Enzo Ferrari (S1 Class)",
            "1965 Ford Mustang GT Coupe (D Class)",
            "2009 Ford Focus RS (B Class)",
            "1970 GMC Jimmy (C Class)",
            "1986 Honda Civic Si (D Class)",
            "2016 Koenigsegg Regera (S2 Class)",
            "2020 Land Rover Defender 110 X (C Class)",
            "2010 Lexus LFA (A Class)",
            "2016 Mazda MX-5 (C Class)",
            "2018 McLaren 600LT Coupé (S1 Class)",
            "1990 Mercedes-Benz 190 E 2.5-16 Evolution II (C Class)",
            "2012 Mercedes-Benz C 63 AMG Coupé Black Series (A Class)",
            "2001 Mitsubishi Lancer Evolution VI GSR TM Edition (B Class)",
            "1987 Nissan Skyline GTS-R (C Class)",
            "1989 Nissan Silvia K's (C Class)",
            "1994 Nissan Fairlady Z Version S Twin Turbo (C Class)",
            "2010 Pagani Zonda Cinque Roadster (S2 Class)",
            "2024 Ram 1500 TRX (B Class)",
            "2018 TVR Griffith (S1 Class)",
            "1992 Toyota Celica GT-Four RC ST185 (C Class)",
            "2023 Toyota Camry TRD (B Class)",
            "2554 AMG Transport Dynamics M12S Warthog CST (A Class)",
            "1962 Ferrari 250 GT Berlinetta Lusso (C Class)",
            "1987 Ferrari F40 (A Class)",
            "2017 Ford #14 Rahal Letterman Lanigan Racing Fiesta (S1 Class)",
            "2017 Ford #25 'Brocky' Ultra4 Bronco RTR (A Class)",
            "2017 Ford Focus RS (B Class)",
            "2024 Ford Mustang Dark Horse (A Class)",
            "1997 Formula Drift #777 Nissan 240SX (S1 Class)",
            "2007 Formula Drift #117 599 GTB Fiorano (S1 Class)",
            "2009 Formula Drift #99 Mazda RX-8 (S1 Class)",
            "2020 Gordon Murray Automotive T.50 (S2 Class)",
            "2005 Honda NSX-R (B Class)",
            "1991 Jaguar Sport XJR-15 (S1 Class)",
            "2017 Koenigsegg Agera RS (S2 Class)",
            "2019 Lamborghini Urus (A Class)",
            "2024 Lamborghini Revuelto (S2 Class)",
            "2015 Land Rover Range Rover Sport SVR (A Class)",
            "1997 Maserati Ghibli Cup (B Class)",
            "1992 Mazda RX-7 Type R (B Class)",
            "2017 Mazda MX-5 Cup (B Class)",
            "2013 Mercedes-Benz G 65 AMG (B Class)",
            "2024 Nissan GT-R Nismo (S1 Class)",
            "1984 Opel Manta 400 (B Class)",
            "2021 Polaris RZR Pro XP Ultimate (C Class)",
            "1970 Porsche #3 917 LH (S1 Class)",
            "2012 Porsche 911 GT3 RS 4.0 (S1 Class)",
            "2014 Porsche 918 Spyder (S2 Class)",
            "2022 Porsche 718 Cayman GT4 RS (S1 Class)",
            "2016 RJ Anderson #37 Polaris RZR Pro 2 Truck (A Class)",
            "1997 Toyota Chaser 2.5 Tourer V (B Class)",
            "1963 Volkswagen Type 2 De Luxe (D Class)",
            "2016 Ariel Nomad (A Class)",
            "2022 Aston Martin Valkyrie AMR Pro (R Class)",
            "2019 BMW Z4 Roadster (A Class)",
            "2021 Bentley Continental GT Convertible (A Class)",
            "1969 Dodge Charger Daytona HEMI (C Class)",
            "2018 Dodge Challenger SRT Demon (A Class)",
            "1984 Honda City E II (D Class)",
            "1991 Honda Beat (D Class)",
            "1994 Honda Acty (D Class)",
            "1994 Honda Prelude Si (C Class)",
            "2023 Honda Civic Type R (A Class)",
            "1986 MG Metro 6R4 (A Class)",
            "1997 Toyota Soarer 2.5 GT-T (C Class)",
            "1998 Toyota Supra RZ (B Class)",
            "2020 Toyota GR Supra (A Class)",
            "1968 Abarth 595 esseesse (D Class)",
            "1980 Abarth Fiat 131 (D Class)",
            "2001 Acura Integra Type R (C Class)",
            "2002 Acura RSX Type S (C Class)",
            "2023 Acura Integra A-Spec (C Class)",
            "1965 Alfa Romeo Giulia Sprint GTA Stradale (D Class)",
            "1968 Alfa Romeo 33 Stradale (B Class)",
            "2007 Alfa Romeo 8C Competizione (A Class)",
            "2017 Alfa Romeo Giulia Quadrifoglio (A Class)",
            "2015 Alumicraft Class 10 Race Car (B Class)",
            "2021 Alumicraft #122 Class 1 Buggy (B Class)",
            "2022 Alumicraft #6165 Trick Truck (C Class)",
            "2013 Ariel Atom 500 V8 (S2 Class)",
            "2017 Aston Martin DB11 (A Class)",
            "2017 Aston Martin Vulcan AMR Pro (S2 Class)",
            "2023 Aston Martin Valkyrie (R Class)",
            "1986 Audi #2 Audi Sport quattro S1 (S1 Class)",
            "2001 Audi RS 4 Avant (B Class)",
            "2003 Audi RS 6 (B Class)",
            "2006 Audi RS 4 (B Class)",
            "2009 Audi R8 LMS (S2 Class)",
            "2009 Audi RS 6 (B Class)",
            "2010 Audi TT RS Coupé (B Class)",
            "2011 Audi RS 3 Sportback (B Class)",
            "2011 Audi RS 5 Coupé (A Class)",
            "2013 Audi RS 4 Avant (A Class)",
            "2013 Audi RS 7 Sportback (A Class)",
            "2015 Audi RS 6 Avant (A Class)",
            "2015 Audi S1 (B Class)",
            "2016 Audi R8 V10 plus (S1 Class)",
            "2018 Audi RS 4 Avant (A Class)",
            "2020 Audi R8 V10 performance (S1 Class)",
            "2020 Audi RS 3 Sedan (A Class)",
            "2021 Audi RS 6 Avant (A Class)",
            "2021 Audi RS 7 Sportback (A Class)",
            "2021 Audi RS e-tron GT (A Class)",
            "1965 Austin-Healey 3000 MkIII (D Class)",
            "1993 Autozam AZ-1 (D Class)",
            "2014 BAC Mono (S1 Class)",
            "1957 BMW Isetta 300 Export (D Class)",
            "1973 BMW 2002 Turbo (C Class)",
            "1988 BMW M3 (C Class)",
            "1988 BMW M5 (C Class)",
            "1995 BMW 850CSi (C Class)",
            "1995 BMW M5 (B Class)",
            "1997 BMW M3 (B Class)",
            "2003 BMW M5 (B Class)",
            "2005 BMW M3 (B Class)",
            "2008 BMW M3 (A Class)",
            "2008 BMW Z4 M Coupé (B Class)",
            "2009 BMW M5 (B Class)",
            "2010 BMW M3 GTS (A Class)",
            "2011 BMW X5 M (B Class)",
            "2012 BMW M5 (A Class)",
            "2014 BMW M4 Coupé (A Class)",
            "2015 BMW i8 (A Class)",
            "2016 BMW M4 GTS (S1 Class)",
            "2020 BMW M8 Competition Coupé (A Class)",
            "2021 BMW M4 Competition Coupé (A Class)",
            "2022 BMW M5 CS (S1 Class)",
            "2022 BMW iX xDrive50 (B Class)",
            "2023 BMW M2 (A Class)",
            "2024 BMW X6 M Competition (A Class)",
            "2013 Cadillac XTS Limousine (D Class)",
            "2016 Cadillac ATS-V (A Class)",
            "2016 Cadillac CTS-V Sedan (A Class)",
            "2022 Cadillac CT4-V Blackwing (A Class)",
            "2022 Cadillac CT5-V Blackwing (S1 Class)",
            "2018 Can-Am Maverick X RS Turbo R (B Class)",
            "1953 Chevrolet Corvette (D Class)",
            "1955 Chevrolet 150 Utility Sedan (D Class)",
            "1957 Chevrolet Bel Air (D Class)",
            "1964 Chevrolet Impala Super Sport 409 (C Class)",
            "1969 Chevrolet Camaro Super Sport Coupe (C Class)",
            "1969 Chevrolet Nova Super Sport 396 (C Class)",
            "1970 Chevrolet Camaro Z28 (C Class)",
            "1970 Chevrolet Chevelle Super Sport 454 (C Class)",
            "1970 Chevrolet Corvette ZR-1 (C Class)",
            "1970 Chevrolet El Camino Super Sport 454 (C Class)",
            "1972 Chevrolet K-10 Custom (D Class)",
            "1979 Chevrolet Camaro Z28 (D Class)",
            "1988 Chevrolet Monte Carlo Super Sport (D Class)",
            "1995 Chevrolet Corvette ZR-1 (B Class)",
            "1996 Chevrolet Impala Super Sport (C Class)",
            "2002 Chevrolet Corvette Z06 (A Class)",
            "2009 Chevrolet Corvette ZR1 (S1 Class)",
            "2015 Chevrolet Camaro Z/28 (A Class)",
            "2015 Chevrolet Corvette Z06 (S1 Class)",
            "2017 Chevrolet Camaro ZL1 (S1 Class)",
            "2018 Chevrolet Camaro ZL1 1LE (S1 Class)",
            "2020 Chevrolet Corvette Stingray Coupe (A Class)",
            "2020 Chevrolet Silverado LT Trail Boss (C Class)",
            "2023 Chevrolet Corvette Z06 (S1 Class)",
            "1970 Datsun 510 (D Class)",
            "2013 DeBerti Jeep Wrangler Unlimited (A Class)",
            "2018 DeBerti Chevrolet Silverado 1500 Drift Truck (S1 Class)",
            "2019 DeBerti Ford Super Duty F-250 Lariat 'Transformer' (B Class)",
            "2019 DeBerti Toyota Tacoma TRD ‘The Performance Truck’ (S1 Class)",
            "1982 DeLorean DMC-12 (D Class)",
            "1970 Dodge Coronet Super Bee (C Class)",
            "2008 Dodge Viper SRT-10 ACR (S1 Class)",
            "2015 Dodge Challenger SRT Hellcat (A Class)",
            "2015 Dodge Charger SRT Hellcat (A Class)",
            "2022 Dodge Challenger SRT Super Stock (A Class)",
            "1962 Ferrari 250 GTO (C Class)",
            "1967 Ferrari #24 Ferrari Spa 330 P4 (A Class)",
            "1969 Ferrari Dino 246 GT (C Class)",
            "1970 Ferrari 512 S (S1 Class)",
            "1989 Ferrari F40 Competizione (R Class)",
            "1995 Ferrari F50 (A Class)",
            "2005 Ferrari FXX (S2 Class)",
            "2007 Ferrari 430 Scuderia (S1 Class)",
            "2009 Ferrari 458 Italia (S1 Class)",
            "2010 Ferrari 599XX (S2 Class)",
            "2013 Ferrari 458 Speciale (S1 Class)",
            "2013 Ferrari LaFerrari (S2 Class)",
            "2014 Ferrari FXX K (R Class)",
            "2015 Ferrari 488 GTB (S1 Class)",
            "2015 Ferrari F12tdf (S1 Class)",
            "2017 Ferrari 812 Superfast (S1 Class)",
            "2017 Ferrari J50 (S1 Class)",
            "2018 Ferrari FXX-K Evo (R Class)",
            "2018 Ferrari Portofino (S1 Class)",
            "2019 Ferrari 488 Pista (S2 Class)",
            "2019 Ferrari Monza SP2 (S1 Class)",
            "2020 Ferrari SF90 Stradale (S2 Class)",
            "1932 Ford De Luxe Five-Window Coupe (D Class)",
            "1966 Ford #2 GT40 Mk II (A Class)",
            "1968 Ford Mustang GT 2+2 Fastback (D Class)",
            "1969 Ford Mustang Boss 302 (C Class)",
            "1973 Ford Capri RS3100 (D Class)",
            "1973 Ford XB Falcon GT (C Class)",
            "1977 Ford #5 Escort RS1800 MkII (B Class)",
            "1986 Ford F-150 XLT Lariat (D Class)",
            "1992 Ford Escort RS Cosworth (C Class)",
            "1993 Ford Mustang SVT Cobra R (C Class)",
            "1994 Ford Supervan 3 (S1 Class)",
            "1999 Ford Racing Puma (C Class)",
            "2000 Ford Mustang SVT Cobra R (B Class)",
            "2001 Ford #4 Ford Focus RS (A Class)",
            "2003 Ford Focus RS (C Class)",
            "2010 Ford Crown Victoria Police Interceptor (D Class)",
            "2011 Ford Transit SuperSportVan (D Class)",
            "2013 Ford Mustang Shelby GT500 (A Class)",
            "2014 Ford #11 Rockstar F-150 Trophy Truck (A Class)",
            "2014 Ford FPV Limited Edition Pursuit Ute (B Class)",
            "2016 Ford Mustang Shelby GT350R (S1 Class)",
            "2017 Ford GT (S1 Class)",
            "2018 Ford Mustang RTR Spec 5 (A Class)",
            "2020 Ford #2069 Ford Performance Bronco R (C Class)",
            "2020 Ford Mustang Shelby GT500 (S1 Class)",
            "2020 Ford Super Duty F-450 DRW PLATINUM (D Class)",
            "2022 Ford Bronco Raptor (C Class)",
            "2022 Ford Focus ST (B Class)",
            "2023 Ford F-150 Raptor R (B Class)",
            "2023 Ford Fiesta ST (C Class)",
            "2024 Ford Mustang GT (A Class)",
            "1989 Formula Drift #98 BMW 325i (S1 Class)",
            "1995 Formula Drift #34 Toyota Supra MkIV (S1 Class)",
            "2013 Formula Drift #777 Chevrolet Corvette (S1 Class)",
            "2016 Formula Drift #530 HSV Maloo GEN-F (S1 Class)",
            "2019 Formula Drift #411 Toyota Corolla Hatchback (S1 Class)",
            "2020 Formula Drift #151 Toyota GR Supra (S1 Class)",
            "2020 Formula Drift #91 BMW M2 (S1 Class)",
            "2023 Formula Drift #64 Forsberg Racing Nissan Z (S1 Class)",
            "1991 GMC Syclone (C Class)",
            "1992 GMC Typhoon (C Class)",
            "2022 GMC HUMMER EV Pickup (A Class)",
            "2025 GR GT Prototype (S1 Class)",
            "2014 HSV GEN-F GTS (A Class)",
            "2014 HSV Limited Edition GEN-F GTS Maloo (A Class)",
            "2019 Hennessey Ford F-150 VelociRaptor 6X6 (B Class)",
            "2021 Hennessey Venom F5 (S2 Class)",
            "1977 Holden Torana A9X (C Class)",
            "1970 Honda S800 (D Class)",
            "1992 Honda NSX-R (B Class)",
            "1997 Honda Civic Type R (C Class)",
            "2003 Honda S2000 (B Class)",
            "2004 Honda Civic Type R (C Class)",
            "2007 Honda Civic Type R (C Class)",
            "2015 Honda Civic Type R (B Class)",
            "2015 Honda Ridgeline Baja Trophy Truck (B Class)",
            "2018 Honda Civic Type R (A Class)",
            "2022 Honda e (D Class)",
            "2019 Hyundai Veloster N (B Class)",
            "2020 Hyundai i30 N (B Class)",
            "2021 Hyundai i20 N (B Class)",
            "2022 Hyundai N Vision 74 (A Class)",
            "2023 Hyundai IONIQ 5 N (A Class)",
            "1956 Jaguar D-Type (B Class)",
            "1964 Jaguar Lightweight E-Type (B Class)",
            "1993 Jaguar XJ220 (A Class)",
            "1993 Jaguar XJ220S TWR (S1 Class)",
            "2010 Jaguar C-X75 (S2 Class)",
            "2012 Jeep Wrangler Rubicon (D Class)",
            "2016 Jeep Trailcat (A Class)",
            "2018 Jeep Grand Cherokee Trackhawk (A Class)",
            "2020 Jeep JT (D Class)",
            "2019 Jimco #240 Fastball Racing Class 6100 Spec Trophy Truck (B Class)",
            "2020 Jimco #179 Hammerhead Class 1 (A Class)",
            "2018 KTM X-Bow GT4 (S1 Class)",
            "2008 Koenigsegg CCGT (S2 Class)",
            "2011 Koenigsegg Agera (S2 Class)",
            "2020 Koenigsegg Jesko (S2 Class)",
            "1967 Lamborghini Miura P400 (B Class)",
            "2010 Lamborghini Murciélago LP 670-4 SV (S1 Class)",
            "2012 Lamborghini Gallardo LP570-4 Spyder Performante (A Class)",
            "2013 Lamborghini Veneno (S2 Class)",
            "2018 Lamborghini Aventador SVJ (S1 Class)",
            "2020 Lamborghini Essenza SCV12 (R Class)",
            "2020 Lamborghini Huracán STO (S1 Class)",
            "2020 Lamborghini Sián Roadster (S1 Class)",
            "2021 Lamborghini Countach LPI 800-4 (S1 Class)",
            "2022 Lamborghini Huracán Tecnica (S1 Class)",
            "1986 Lancia Delta S4 (B Class)",
            "1992 Lancia Delta HF Integrale EVO (C Class)",
            "2015 Lexus RC F (A Class)",
            "2021 Lexus LC 500 (B Class)",
            "1997 Lotus Elise GT1 (S1 Class)",
            "1999 Lotus Elise Series 1 Sport 190 (B Class)",
            "2020 Lotus Evija (R Class)",
            "2024 Lucid Air Sapphire (S2 Class)",
            "1965 MINI Cooper S (D Class)",
            "2012 MINI John Cooper Works GP (B Class)",
            "2013 MINI X-Raid All4 Racing Countryman (B Class)",
            "2008 Maserati MC12 Versione Corsa (R Class)",
            "2022 Maserati MC20 (S1 Class)",
            "1973 Mazda RX-3 (D Class)",
            "1990 Mazda Savanna RX-7 (C Class)",
            "1994 Mazda MX-5 Miata (D Class)",
            "2005 Mazda Mazdaspeed MX-5 (C Class)",
            "2010 Mazda Mazdaspeed 3 (B Class)",
            "2011 Mazda RX-8 R3 (B Class)",
            "2013 Mazda MX-5 (C Class)",
            "2022 Mazda MX-5 Miata RF (B Class)",
            "1993 McLaren F1 (S1 Class)",
            "1997 McLaren F1 GT (S1 Class)",
            "2011 McLaren 12C Coupé (S1 Class)",
            "2013 McLaren P1 (S2 Class)",
            "2014 McLaren 650S Spider (S1 Class)",
            "2015 McLaren 570S Coupé (S1 Class)",
            "2019 McLaren Speedtail (S2 Class)",
            "2021 McLaren 765LT Coupé (S2 Class)",
            "2023 McLaren Artura (S1 Class)",
            "2015 Mercedes-AMG GT S (A Class)",
            "2016 Mercedes-AMG C 63 S Coupé (A Class)",
            "2018 Mercedes-AMG E 63 S (A Class)",
            "2020 Mercedes-AMG GT Black Series (S1 Class)",
            "2020 Mercedes-AMG SLC 43 Final Edition (A Class)",
            "2021 Mercedes-AMG Mercedes-AMG ONE (S2 Class)",
            "2021 Mercedes-AMG SL 63 (A Class)",
            "1954 Mercedes-Benz 300 SL Coupé (D Class)",
            "1955 Mercedes-Benz 300 SLR (B Class)",
            "1987 Mercedes-Benz AMG Hammer Coupe (B Class)",
            "2009 Mercedes-Benz SL 65 AMG Black Series (A Class)",
            "2013 Mercedes-Benz A 45 AMG (B Class)",
            "2014 Mercedes-Benz Unimog U5023 (D Class)",
            "2018 Mercedes-Benz X-Class (D Class)",
            "1971 Meyers Manx (D Class)",
            "2023 Meyers Manx 2.0 (B Class)",
            "1992 Mitsubishi Galant VR-4 (C Class)",
            "1995 Mitsubishi Eclipse GSX (C Class)",
            "1995 Mitsubishi Montero Exceed 2800 TD (D Class)",
            "1997 Mitsubishi GTO (C Class)",
            "2004 Mitsubishi Lancer Evolution VIII MR (B Class)",
            "2008 Mitsubishi Lancer Evolution X GSR (B Class)",
            "1969 Nissan Fairlady Z 432 (D Class)",
            "1973 Nissan Skyline H/T 2000GT-R (C Class)",
            "1989 Nissan S-Cargo (D Class)",
            "1990 Nissan Pulsar GTI-R (C Class)",
            "1992 Nissan Skyline GT-R (B Class)",
            "1994 Nissan Silvia K's (C Class)",
            "1995 Nissan Gloria Gran Turismo (C Class)",
            "1995 Nissan NISMO GT-R LM (B Class)",
            "1997 Nissan Stagea RS Four V (C Class)",
            "1998 Nissan Silvia K's Aero (C Class)",
            "2000 Nissan Skyline GT-R V Spec II (B Class)",
            "2002 Nissan Silvia Spec-R (B Class)",
            "2003 Nissan Fairlady Z (B Class)",
            "2012 Nissan GT-R Black Edition (R35) (S1 Class)",
            "2017 Nissan GT-R (R35) (S1 Class)",
            "2019 Nissan 370Z Nismo (A Class)",
            "2020 Nissan GT-R NISMO (R35) (S1 Class)",
            "2024 Nissan Z NISMO (A Class)",
            "2010 Noble M600 (S1 Class)",
            "2009 Pagani Zonda R (R Class)",
            "2016 Pagani Huayra BC Coupe (S2 Class)",
            "1962 Peel P50 (D Class)",
            "2011 Penhall The Cholla (B Class)",
            "1991 Peugeot 205 Rallye (D Class)",
            "1958 Plymouth Fury (D Class)",
            "1968 Plymouth Barracuda Formula S (C Class)",
            "1971 Plymouth Cuda 426 HEMI (C Class)",
            "2021 Polaris RZR Pro XP Factory Racing Limited Edition (C Class)",
            "1977 Pontiac Firebird Trans Am (D Class)",
            "1987 Pontiac Firebird Trans Am GTA (D Class)",
            "1973 Porsche 911 Carrera RS (C Class)",
            "1985 Porsche #185 959 Prodrive Rally Raid (A Class)",
            "1989 Porsche 944 Turbo (B Class)",
            "1993 Porsche 928 GTS (B Class)",
            "1993 Porsche 968 Turbo S (B Class)",
            "1997 Porsche 911 GT1 Strassenversion (S1 Class)",
            "2004 Porsche 911 GT3 (A Class)",
            "2005 Porsche Cayman GT3 WTAC (S2 Class)",
            "2018 Porsche 718 Cayman GTS (A Class)",
            "2018 Porsche 911 GT2 RS (S2 Class)",
            "2018 Porsche Cayenne Turbo (A Class)",
            "2018 Porsche Macan LPR Rally Raid (B Class)",
            "2019 Porsche #70 Porsche Motorsport 935 (S2 Class)",
            "2019 Porsche 911 Carrera S (S1 Class)",
            "2020 Porsche Taycan Turbo S (S1 Class)",
            "2021 Porsche 911 GT3 (S1 Class)",
            "2021 Porsche Mission R (S2 Class)",
            "2023 Porsche 911 GT3 RS (S1 Class)",
            "2023 Porsche 911 Turbo S (S1 Class)",
            "2015 Radical RXC Turbo (S2 Class)",
            "1972 Reliant Supervan III (D Class)",
            "1980 Renault 5 Turbo (C Class)",
            "1993 Renault Clio Williams (D Class)",
            "2008 Renault Mégane R26.R (B Class)",
            "2010 Renault Megane RS 250 (B Class)",
            "2018 Renault Megane R.S. (B Class)",
            "2022 Rivian R1T (A Class)",
            "2020 SIERRA Cars #23 Yokohama ALPHA (R Class)",
            "2021 SIERRA Cars 700R (D Class)",
            "2021 SIERRA Cars RX3 (A Class)",
            "1965 Shelby Cobra Daytona Coupe (B Class)",
            "1980 Subaru BRAT GL (D Class)",
            "1990 Subaru LEGACY RS (C Class)",
            "1994 Subaru Vivio RX-R (D Class)",
            "1996 Subaru SVX (C Class)",
            "1998 Subaru Impreza 22B-STi Version (B Class)",
            "2004 Subaru IMPREZA WRX STI (B Class)",
            "2005 Subaru IMPREZA WRX STI (B Class)",
            "2005 Subaru LEGACY B4 2.0 GT (B Class)",
            "2008 Subaru IMPREZA WRX STI (B Class)",
            "2011 Subaru WRX STI (B Class)",
            "2013 Subaru BRZ (C Class)",
            "2015 Subaru WRX STI (B Class)",
            "2022 Subaru BRZ (B Class)",
            "2022 Subaru WRX (B Class)",
            "2005 TVR Sagaris (A Class)",
            "1979 Toyota FJ40 (D Class)",
            "1985 Toyota Sprinter Trueno GT Apex (D Class)",
            "1991 Toyota Chaser GT Twin Turbo (C Class)",
            "1991 Toyota Sera (D Class)",
            "1992 Toyota Supra 2.0 GT (C Class)",
            "1993 Toyota #1 T100 Baja Truck (B Class)",
            "1994 Toyota Celica GT-Four ST205 (C Class)",
            "1995 Toyota MR2 GT (B Class)",
            "2003 Toyota Celica Sport Specialty II (C Class)",
            "2005 Toyota Crown Super Deluxe Taxi (D Class)",
            "2013 Toyota 86 (C Class)",
            "2017 Toyota JPN Taxi (D Class)",
            "2019 Toyota 4Runner TRD Pro (C Class)",
            "2019 Toyota Tacoma TRD Pro (C Class)",
            "2021 Toyota GR Yaris (B Class)",
            "2022 Toyota GR86 (B Class)",
            "2025 Toyota Land Cruiser (C Class)",
            "2015 Ultima Evolution Coupe 1020 (R Class)",
            "1963 Volkswagen Beetle (D Class)",
            "1969 Volkswagen Class 5/1600 Baja Bug (D Class)",
            "1982 Volkswagen Pickup LX (D Class)",
            "1983 Volkswagen Golf GTI (D Class)",
            "1992 Volkswagen Golf Gti 16v Mk2 (D Class)",
            "1995 Volkswagen Corrado VR6 (C Class)",
            "2010 Volkswagen Golf R (B Class)",
            "2011 Volkswagen Scirocco R (B Class)",
            "2014 Volkswagen Golf R (B Class)",
            "2017 Volkswagen #34 Andretti Rally Cross Beetle (S1 Class)",
            "2021 Volkswagen Golf R (B Class)",
            "2022 Volkswagen Golf R (B Class)",
            "1983 Volvo 242 Turbo Evolution (C Class)",
            "2013 Wuling Sunshine S (D Class)",
            "2022 Wuling Hongguang Mini EV (D Class)",
            "2019 Zenvo TSR-S (R Class)",
            "2016 Aston Martin Vulcan (S2 Class)",
            "2024 Chevrolet Corvette E-Ray (S1 Class)",
            "2014 Lamborghini Huracán LP 610-4 (S1 Class)",
            "2016 Lamborghini Centenario LP 770-4 (S1 Class)",
            "2013 SRT Viper GTS (S1 Class)",
        ]
        
    @functools.cached_property
    def wristband_cars(self) -> List[str]:
        return [
            "2023 Porsche 911 Rallye (A Class)",
            "2020 BMW M2 Competition Coupé (A Class)",
            "2022 Lamborghini Aventador LP 780-4 Ultimae (S1 Class)",
            "2018 Subaru WRX STI ARX Supercar (S1 Class)",
            "2022 Acura NSX Type S (S1 Class)",
            "2007 Peugeot 207 Super 2000 (A Class)",
            "1985 Ford RS200 Evolution (S1 Class)",
        ]
        
    @functools.cached_property
    def collection_cars(self) -> List[str]:
        return [
            "1981 BMW M1 (B Class)",
            "1969 Dodge Charger R/T (C Class)",
            "1987 Ford Sierra Cosworth RS500 (C Class)",
            "2005 Ford GT (A Class)",
            "2005 Honda NSX-R GT (A Class)",
            "1997 Lamborghini Diablo SV (A Class)",
            "1974 Lancia Stratos HF Stradale (C Class)",
            "1962 Lincoln Continental (D Class)",
            "1985 Mazda RX-7 GSL-SE (D Class)",
            "1991 Mazda #55 Mazda 787B (R Class)",
            "1995 Mitsubishi Lancer Evolution III GSR (B Class)",
            "1997 Mitsubishi Montero Evolution (D Class)",
            "2005 Mitsubishi #1 Sierra Sierra Enterprises Lancer Evolution Time Attack (R Class)",
            "1971 Nissan Skyline 2000GT-R (D Class)",
            "1983 Nissan #11 Tomica Skyline Turbo Super Silhouette (S2 Class)",
            "1985 Nissan Safari Turbo (D Class)",
            "1989 Nissan PAO (D Class)",
            "1991 Nissan Figaro (D Class)",
            "1998 Nissan #23 Pennzoil NISMO Skyline GT-R (S2 Class)",
            "1998 Nissan R390 (GT1) (S1 Class)",
            "1984 Peugeot 205 Turbo 16 (C Class)",
            "1982 Porsche 911 Turbo 3.3 (B Class)",
            "1987 Porsche 959 (A Class)",
            "1969 Toyota 2000GT (D Class)",
            "1965 Alfa Romeo Giulia TZ2 (B Class)",
            "2013 Audi R8 Coupé V10 plus 5.2 FSI quattro (A Class)",
            "2023 BMW M2 Forza Edition (A Class)",
            "1967 Chevrolet Corvette Stingray 427 (B Class)",
            "2021 Dodge Durango SRT Hellcat (A Class)",
            "1996 Ferrari F50 GT (R Class)",
            "2022 Ford Supervan 4 (R Class)",
            "2018 Funco Motorsports F9 (S1 Class)",
            "1974 Honda Civic RS (D Class)",
            "1984 Honda Civic CRX Mugen (D Class)",
            "2022 Lamborghini Huracán Sterrato (S1 Class)",
            "2010 Lexus LFA Forza Edition (S2 Class)",
            "2018 Lotus Scura Motorsports Exige WTAC (R Class)",
            "2018 MINI X-raid John Cooper Works Buggy (B Class)",
            "2003 Porsche Carrera GT (S1 Class)",
            "1965 Shelby Cobra 427 S/C (B Class)",
            "1994 Subaru Vivio RX-R Forza Edition (S2 Class)",
            "1985 Toyota Sprinter Trueno GT Apex Forza Edition (B Class)",
            "2013 Toyota 86 Stories (A Class)",
            "1965 Toyota Sports 800 (D Class)",
        ]
    
    @functools.cached_property
    def playlist_history_cars(self) -> List[str]:
        return [
            "1972 Mazda Cosmo 110S Series II (D Class)",
        ]
    
    @functools.cached_property
    def playlist_welcome_to_japan_cars(self) -> List[str]:
        return [
            # Series
            "2008 Mazda Furai (R Class)",
            "2010 Nissan 370Z (B Class)",
            
            # Summer
            "1999 Toyota Altezza RS200 Z EDITION (C Class)",
            "2006 Mitsubishi Lancer Evolution IX MR (B Class)",
            
            # Autumn
            "1997 Nissan Skyline GT-R V-Spec (B Class)",
            "1991 Honda CR-X SiR (C Class)",
            
            # Winter
            "2019 Subaru STI S209 (B Class)",
            "2016 Toyota Land Cruiser Arctic Trucks AT37 (D Class)",
            
            # Spring
            "1996 Toyota Starlet Glanza V (C Class)",
            "1974 Toyota Corolla SR5 (D Class)",
            
            # Exclusive Reward
            "1989 Toyota MR2 SC (D Class)",
            "2021 Pagani Huayra R (R Class)",
            "2021 McLaren Sabre (S1 Class)",
            "2022 Ferrari 296 GTB (S2 Class)",
            "2016 Abarth 695 Biposto (B Class)",
            "1993 Schuppan 962CR (S1 Class)",
            "2021 Aston Martin DBX (A Class)",
            "1987 Nissan Be-1 (D Class)",
            "2020 Lamborghini Huracán EVO (S1 Class)",
            "2023 Lotus Emira (A Class)",
            "1969 Datsun 2000 Roadster (D Class)",
            "2020 Ferrari Roma (S1 Class)",
            "1967 Renault 8 Gordini (D Class)",
            "1988 Lamborghini Countach LP5000 QV (A Class)",
            "2004 Maserati MC12 (S1 Class)",
            "1994 Ferrari F355 Berlinetta (B Class)",
            "2017 Saleen S7 LM (S2 Class)",
        ]
    
    @functools.cached_property
    def playlist_horizon_decades_cars(self) -> List[str]:
        return [
            # Series
            "1993 Porsche 911 Turbo S Leichtbau (A Class)",
            "2018 Lotus Exige Cup 430 (S1 Class)",
            
            # Summer
            "1989 Volkswagen Rallye Golf (C Class)",
            "1988 Lamborghini Countach LP5000 QV (A Class)",
            
            # Autumn
            "1998 TVR Cerbera Speed 12 (S1 Class)",
            "1993 Schuppan 962CR (S1 Class)",
            
            # Winter
            "2006 Dodge Ram SRT-10 (B Class)",
            "2003 Ford F-150 SVT Lightning (C Class)",
            
            # Spring
            "2017 Mercedes-AMG GT R (S1 Class)",
            "2017 Saleen S7 LM (S2 Class)",
            
            # Exclusive Reward
            "1999 Lamborghini Diablo GTR (S2 Class)",
        ]
    
    @functools.cached_property
    def playlist_italian_exotics_cars(self) -> List[str]:
        return [
            # Series
            "2024 Lamborghini Temerario (S2 Class)",
            "2022 Ferrari 296 GTB (S2 Class)",
            
            # Summer
            "1984 De Tomaso Pantera GT5 (B Class)",
            "2004 Maserati MC12 (S1 Class)",
            
            # Autumn
            "2017 Abarth 124 Spider (C Class)",
            "2020 Lamborghini Huracán EVO (S1 Class)",
            
            # Winter
            "1982 Lancia 037 Stradale (B Class)",
            "2020 Ferrari Roma (S1 Class)",
            
            # Spring
            "2022 Lamborghini Huracán EVO Spyder (S1 Class)",
            "2021 Pagani Huayra R (R Class)",
            
            # Exclusive Reward
        ]
    
    @functools.cached_property
    def playlist_horizon_mascot_party_cars(self) -> List[str]:
        return [
            # Series
            "1970 Honda N600 (D Class)",
            "1967 Renault 8 Gordini (D Class)",
            
            # Summer
            "2018 Exomotive V8 XP-5 (S2 Class)",
            "1969 Datsun 2000 Roadster (D Class)",
            
            # Autumn
            "2024 Chevrolet Camaro ZL1 (S1 Class)",
            "2016 Abarth 695 Biposto (B Class)",
            
            # Winter
            "1974 Toyota Celica GT (D Class)",
            "1989 Toyota MR2 SC (D Class)",
            
            # Spring
            "1988 Mitsubishi Starion ESI-R (C Class)",
            "1968 Dodge Dart HEMI Super Stock (B Class)",
            
            # Exclusive Reward
        ]
    
    @functools.cached_property
    def wheelspin_cars(self) -> List[str]:
        return [
            "2019 Apollo Intensa Emozione (R Class)",
            "2019 Aston Martin DBS Superleggera (S1 Class)",
            "2019 Aston Martin Valhalla Concept Car (R Class)",
            "1984 Audi Sport quattro (B Class)",
            "2020 BMW M2 Competition Coupé (A Class)",
            "2016 Bentley Bentayga (A Class)",
            "2019 Casey Currie Motorsports #4402 Ultra 4 'Trophy Jeep' (A Class)",
            "1960 Chevrolet Corvette (C Class)",
            "2019 Chevrolet Corvette ZR1 (S1 Class)",
            "1968 Dodge Dart HEMI Super Stock (B Class)",
            "1970 Dodge Challenger R/T (C Class)",
            "2016 Dodge Viper ACR (S1 Class)",
            "1984 Ferrari 288 GTO (A Class)",
            "1992 Ferrari 512 TR (A Class)",
            "1994 Ferrari F355 Berlinetta (B Class)",
            "2012 Ferrari 599XX Evolution (S2 Class)",
            "2019 Ferrari F8 Tributo (S2 Class)",
            "1968 Ford Mustang GT 2+2 Fastback Forza Edition (A Class)",
            "1986 Ford F-150 XLT Lariat Forza Edition (S2 Class)",
            "2014 Ford Ranger T6 Rally Raid (B Class)",
            "2017 Ford M-Sport Fiesta RS (S1 Class)",
            "2020 Ford Super Duty F-450 DRW PLATINUM Forza Edition (A Class)",
            "2022 Ford F-150 Lightning (C Class)",
            "2006 Formula Drift #43 Dodge Viper SRT-10 ACR (S1 Class)",
            "2015 Formula Drift #13 Ford Mustang (S1 Class)",
            "2012 Hennessey Venom GT (S2 Class)",
            "1961 Jaguar E-type (C Class)",
            "2015 Koenigsegg One:1 (S2 Class)",
            "1999 Lamborghini Diablo GTR (S2 Class)",
            "2011 Lamborghini Sesto Elemento (S2 Class)",
            "2012 Lamborghini Aventador LP700-4 (S1 Class)",
            "2021 McLaren 620R (S1 Class)",
            "2018 Mercedes-AMG GT 4-Door Coupé (A Class)",
            "1990 Mercedes-Benz 190 E 2.5-16 Evolution II Forza Edition (A Class)",
            "1998 Mercedes-Benz AMG CLK GTR (S1 Class)",
            "2014 Mercedes-Benz G 63 AMG 6x6 (C Class)",
            "1989 Nissan S-Cargo Forza Edition (S1 Class)",
            "1993 Nissan 240SX (D Class)",
            "2012 Nissan GT-R Black Edition (R35) Forza Edition (S2 Class)",
            "1970 Porsche #3 917 LH Forza Edition (R Class)",
            "1995 Porsche 911 GT2 (A Class)",
            "2019 Porsche 911 GT3 RS (S1 Class)",
            "2021 RJ Anderson #37 Polaris RZR Pro 4 Truck (A Class)",
            "2021 Rimac Nevera (R Class)",
            "2013 Wuling Sunshine S Forza Edition (S1 Class)",
        ]
        
    @functools.cached_property
    def car_pass_cars(self) -> List[str]:
        return [
            "2003 Aston Martin DB7 GT (B Class)",
            "2023 Audi R8 Coupé V10 GT RWD (S1 Class)",
            "1972 Datsun #269 Attacking the Clock Racing 240Z 'All Carbon Hill Climb Beast' (R Class)",
            "1972 Honda Z GT (D Class)",
            "2008 Honda Civic Type R (FD2) (B Class)",
            "2024 Koenigsegg Gemera (S2 Class)",
            "1974 Mazda #123 Mad Mike 808 Wagon 'FURSTY' (S1 Class)",
            "1972 Nissan Patrol (D Class)",
            "1990 Nissan #12 Skyline GT-R (BNR32 Gr.A) JTC (S2 Class)",
            "1998 Nissan Skyline GT-R 40th Anniversary (B Class)",
            "2023 Toyota GR Corolla (B Class)",
            "2024 Toyota Prius Prime XSE Premium (C Class)",
            "1968 Alfa Romeo Autodelta Tipo 33/2 Daytona (A Class)",
            "1957 Ford Thunderbird (D Class)",
            "1983 Nissan Skyline 2000 Turbo RS (C Class)",
            "1987 Porsche #203 Porsche AG 961 (S2 Class)",
        ]
        
    @functools.cached_property
    def italian_passion_cars(self) -> List[str]:
        return [
            "2021 Alfa Romeo Giulia GTAm (S1 Class)",
            "1990 Alfa Romeo SE 048SP (R Class)",
            "1967 Ferrari 275 GTB4 Spider (C Class)",
            "2025 Ferrari F80 (R Class)",
        ]
        
    @functools.cached_property
    def partnership_cars(self) -> List[str]:
        return [
            "1962 Peel P50 Trolli Edition (D Class)",
            "1965 Toyota Sports 800 Fanta Edition (D Class)",
        ]
        
    @functools.cached_property
    def preorder_cars(self) -> List[str]:
        return [
            "2017 Ferrari J50 Preorder Car (S1 Class)",
        ]
        
    @functools.cached_property
    def time_attack_cars(self) -> List[str]:
        return [
            "1990 Honda #19 101 Motorsport CRX WTAC (S2 Class)",
            "1992 Honda #21 Hardrace/JDMYard Civic WTAC (R Class)",
            "2001 Honda #33 Integra WTAC (S2 Class)",
            "2004 Honda #52 Evasive Motorsports S2000 WTAC (S2 Class)",
            "1990 Mitsubishi #269 Attacking the Clock Racing Minicab Time Attack (D Class)",
            "1993 Nissan #32 Skyline WTAC 'Xtreme GTR' (R Class)",
            "2000 Nissan #36 Dream Project S15 Silvia WTAC (R Class)",
            "1995 Toyota J&J Motorsport Supra WTAC (S2 Class)",
        ]
        
    @functools.cached_property
    def vip_cars(self) -> List[str]:
        return [
            "1999 Dodge Viper GTS ACR Forza Edition (A Class)",
            "2020 Lotus Evija Forza Edition (S2 Class)",
            "2019 Toyota Tacoma TRD Pro Forza Edition (R Class)",
        ]
        
    @functools.cached_property
    def welcome_cars(self) -> List[str]:
        return [
            "2021 BMW M4 Competition Coupé Welcome Pack (S1 Class)",
            "2018 Ferrari FXX-K Evo Welcome Pack (R Class)",
            "2023 Ford F-150 Raptor R Welcome Pack (B Class)",
            "2020 Mercedes-AMG GT Black Series Welcome Pack (S2 Class)",
            "2004 Mitsubishi Lancer Evolution VIII MR Welcome Pack (A Class)",
        ]
        
    def cars(self) -> List[str]:
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
    def star_amount_job_range() -> range:
        return range(1, 10)
        
# Archipelago Options
class ForzaHorizon6IncludeChallengeType(OptionSet):
    """Indicates which type of challenge should be included"""
    display_name = "Forza Horizon 6 Challenge Type"
    valid_keys = {
        "Single Race",
        "Championship Race",
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
