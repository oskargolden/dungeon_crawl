# config/npc_catalogue.py
"""A catalogue of all non-monster NPC templates in the game."""

from config.templates import NPCTemplate, MonsterBehavior

TOWNSFOLK = NPCTemplate(
    name="Townsfolk",
    symbol="p",
    description="A local resident.",
    behavior=MonsterBehavior.NEUTRAL,
    base_health=8,
    base_stats={'strength': 10, 'dexterity': 10},
    loot_table=["Copper Coins"]
)

# A master dictionary for easy lookup by name
NPCS = {
    "Townsfolk": TOWNSFOLK,
}
