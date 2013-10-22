from __future__ import unicode_literals

from django.db import models


class Abilities(models.Model):
    # TODO: Merge AbilityNames into here (we only care about English)
    # TODO: Merge AbilityProse into here
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=24)
    generation = models.ForeignKey('Generations')
    is_main_series = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'abilities'


class AbilityFlavorText(models.Model):
    ability = models.ForeignKey(Abilities)
    version_group = models.ForeignKey('VersionGroups')
    language = models.ForeignKey('Languages')
    flavor_text = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'ability_flavor_text'


class AbilityNames(models.Model):
    ability = models.ForeignKey(Abilities)
    local_language = models.ForeignKey('Languages')
    name = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'ability_names'


class AbilityProse(models.Model):
    ability = models.ForeignKey(Abilities)
    local_language = models.ForeignKey('Languages')
    effect = models.CharField(max_length=5120, blank=True)
    short_effect = models.CharField(max_length=512, blank=True)

    class Meta:
        managed = False
        db_table = 'ability_prose'


class EggGroupProse(models.Model):
    egg_group = models.ForeignKey('EggGroups')
    local_language = models.ForeignKey('Languages')
    name = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'egg_group_prose'


class EggGroups(models.Model):
    # TODO: Merge EggGroupProse into here
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'egg_groups'


class EvolutionTriggerProse(models.Model):
    evolution_trigger = models.ForeignKey('EvolutionTriggers')
    local_language = models.ForeignKey('Languages')
    name = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'evolution_trigger_prose'


class EvolutionTriggers(models.Model):
    # TODO: Merge EvolutionTriggerProse into here
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'evolution_triggers'


class Experience(models.Model):
    growth_rate = models.ForeignKey('GrowthRates')
    level = models.IntegerField()
    experience = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'experience'


class GrowthRateProse(models.Model):
    growth_rate = models.ForeignKey('GrowthRates')
    local_language = models.ForeignKey('Languages')
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'growth_rate_prose'


class GrowthRates(models.Model):
    # TODO: Merge GrowthRateProse into here
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=20)
    formula = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'growth_rates'


class ItemFlingEffectProse(models.Model):
    item_fling_effect = models.ForeignKey('ItemFlingEffects')
    local_language = models.ForeignKey('Languages')
    effect = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'item_fling_effect_prose'


class ItemFlingEffects(models.Model):
    # TODO: Merge ItemFlingEffectProse into here
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'item_fling_effects'


class ItemNames(models.Model):
    item = models.ForeignKey('Items')
    local_language = models.ForeignKey('Languages')
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'item_names'


class ItemProse(models.Model):
    item = models.ForeignKey('Items')
    local_language = models.ForeignKey('Languages')
    short_effect = models.CharField(max_length=256, blank=True)
    effect = models.CharField(max_length=5120, blank=True)

    class Meta:
        managed = False
        db_table = 'item_prose'


class Items(models.Model):
    # TODO: Merge ItemProse and ItemNames into here
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=20)
    category = models.ForeignKey(ItemCategories)
    cost = models.IntegerField()
    fling_power = models.IntegerField(blank=True, null=True)
    fling_effect = models.ForeignKey(ItemFlingEffects, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class LocationNames(models.Model):
    location = models.ForeignKey('Locations')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'location_names'


class Locations(models.Model):
    # TODO: Merge LocationNames into here
    id = models.IntegerField(primary_key=True)
    region = models.ForeignKey('Regions', blank=True, null=True)
    identifier = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'locations'


class Machines(models.Model):
    machine_number = models.IntegerField()
    version_group = models.ForeignKey('VersionGroups')
    item = models.ForeignKey(Items)
    move = models.ForeignKey('Moves')

    class Meta:
        managed = False
        db_table = 'machines'


class MoveBattleStyleProse(models.Model):
    move_battle_style = models.ForeignKey('MoveBattleStyles')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'move_battle_style_prose'


class MoveBattleStyles(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'move_battle_styles'


class MoveChangelog(models.Model):
    move = models.ForeignKey('Moves')
    changed_in_version_group = models.ForeignKey('VersionGroups')
    type = models.ForeignKey('Types', blank=True, null=True)
    power = models.SmallIntegerField(blank=True, null=True)
    pp = models.SmallIntegerField(blank=True, null=True)
    accuracy = models.SmallIntegerField(blank=True, null=True)
    effect = models.ForeignKey('MoveEffects', blank=True, null=True)
    effect_chance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_changelog'


class MoveDamageClassProse(models.Model):
    move_damage_class = models.ForeignKey('MoveDamageClasses')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=16, blank=True)
    description = models.CharField(max_length=64, blank=True)

    class Meta:
        managed = False
        db_table = 'move_damage_class_prose'


class MoveDamageClasses(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'move_damage_classes'


class MoveEffectChangelog(models.Model):
    id = models.IntegerField(primary_key=True)
    effect = models.ForeignKey('MoveEffects')
    changed_in_version_group = models.ForeignKey('VersionGroups')

    class Meta:
        managed = False
        db_table = 'move_effect_changelog'


class MoveEffectChangelogProse(models.Model):
    move_effect_changelog = models.ForeignKey(MoveEffectChangelog)
    local_language = models.ForeignKey(Languages)
    effect = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'move_effect_changelog_prose'


class MoveEffectProse(models.Model):
    move_effect = models.ForeignKey('MoveEffects')
    local_language = models.ForeignKey(Languages)
    short_effect = models.CharField(max_length=256, blank=True)
    effect = models.CharField(max_length=5120, blank=True)

    class Meta:
        managed = False
        db_table = 'move_effect_prose'


class MoveEffects(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'move_effects'


class MoveFlagMap(models.Model):
    move = models.ForeignKey('Moves')
    move_flag = models.ForeignKey('MoveFlags')

    class Meta:
        managed = False
        db_table = 'move_flag_map'


class MoveFlagProse(models.Model):
    move_flag = models.ForeignKey('MoveFlags')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=256, blank=True)

    class Meta:
        managed = False
        db_table = 'move_flag_prose'


class MoveFlags(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'move_flags'


class MoveFlavorSummaries(models.Model):
    move = models.ForeignKey('Moves')
    local_language = models.ForeignKey(Languages)
    flavor_summary = models.CharField(max_length=512, blank=True)

    class Meta:
        managed = False
        db_table = 'move_flavor_summaries'


class MoveFlavorText(models.Model):
    move = models.ForeignKey('Moves')
    version_group = models.ForeignKey('VersionGroups')
    language = models.ForeignKey(Languages)
    flavor_text = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'move_flavor_text'


class MoveMeta(models.Model):
    move = models.ForeignKey('Moves', primary_key=True)
    meta_category = models.ForeignKey('MoveMetaCategories')
    meta_ailment = models.ForeignKey('MoveMetaAilments')
    min_hits = models.IntegerField(blank=True, null=True)
    max_hits = models.IntegerField(blank=True, null=True)
    min_turns = models.IntegerField(blank=True, null=True)
    max_turns = models.IntegerField(blank=True, null=True)
    recoil = models.IntegerField()
    healing = models.IntegerField()
    crit_rate = models.IntegerField()
    ailment_chance = models.IntegerField()
    flinch_chance = models.IntegerField()
    stat_chance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'move_meta'


class MoveMetaAilmentNames(models.Model):
    move_meta_ailment = models.ForeignKey('MoveMetaAilments')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'move_meta_ailment_names'


class MoveMetaAilments(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(unique=True, max_length=24)

    class Meta:
        managed = False
        db_table = 'move_meta_ailments'


class MoveMetaCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'move_meta_categories'


class MoveMetaCategoryProse(models.Model):
    move_meta_category = models.ForeignKey(MoveMetaCategories)
    local_language = models.ForeignKey(Languages)
    description = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'move_meta_category_prose'


class MoveMetaStatChanges(models.Model):
    move = models.ForeignKey('Moves')
    stat = models.ForeignKey('Stats')
    change = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'move_meta_stat_changes'


class MoveNames(models.Model):
    move = models.ForeignKey('Moves')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'move_names'


class MoveTargetProse(models.Model):
    move_target = models.ForeignKey('MoveTargets')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=128, blank=True)

    class Meta:
        managed = False
        db_table = 'move_target_prose'


class MoveTargets(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'move_targets'


class Moves(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=24)
    generation = models.ForeignKey(Generations)
    type = models.ForeignKey('Types')
    power = models.SmallIntegerField()
    pp = models.SmallIntegerField(blank=True, null=True)
    accuracy = models.SmallIntegerField(blank=True, null=True)
    priority = models.SmallIntegerField()
    target = models.ForeignKey(MoveTargets)
    damage_class = models.ForeignKey(MoveDamageClasses)
    effect = models.ForeignKey(MoveEffects)
    effect_chance = models.IntegerField(blank=True, null=True)
    contest_type = models.ForeignKey(ContestTypes, blank=True, null=True)
    contest_effect = models.ForeignKey(ContestEffects, blank=True, null=True)
    super_contest_effect = models.ForeignKey('SuperContestEffects', blank=True,
                                             null=True)

    class Meta:
        managed = False
        db_table = 'moves'


class NatureBattleStylePreferences(models.Model):
    nature = models.ForeignKey('Natures')
    move_battle_style = models.ForeignKey(MoveBattleStyles)
    low_hp_preference = models.IntegerField()
    high_hp_preference = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nature_battle_style_preferences'


class NatureNames(models.Model):
    nature = models.ForeignKey('Natures')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'nature_names'


class NaturePokeathlonStats(models.Model):
    nature = models.ForeignKey('Natures')
    pokeathlon_stat = models.ForeignKey('PokeathlonStats')
    max_change = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nature_pokeathlon_stats'


class Natures(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=8)
    decreased_stat = models.ForeignKey('Stats', related_name='+')
    increased_stat = models.ForeignKey('Stats')
    hates_flavor = models.ForeignKey(ContestTypes, related_name='+')
    likes_flavor = models.ForeignKey(ContestTypes)

    class Meta:
        managed = False
        db_table = 'natures'


class PalPark(models.Model):
    species = models.ForeignKey('PokemonSpecies', primary_key=True)
    area = models.ForeignKey('PalParkAreas')
    base_score = models.IntegerField()
    rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pal_park'


class PalParkAreaNames(models.Model):
    pal_park_area = models.ForeignKey('PalParkAreas')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'pal_park_area_names'


class PalParkAreas(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'pal_park_areas'


class PokeathlonStatNames(models.Model):
    pokeathlon_stat = models.ForeignKey('PokeathlonStats')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'pokeathlon_stat_names'


class PokeathlonStats(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'pokeathlon_stats'


class PokedexProse(models.Model):
    pokedex = models.ForeignKey('Pokedexes')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=16, blank=True)
    description = models.CharField(max_length=512, blank=True)

    class Meta:
        managed = False
        db_table = 'pokedex_prose'


class Pokedexes(models.Model):
    id = models.IntegerField(primary_key=True)
    region = models.ForeignKey('Regions', blank=True, null=True)
    identifier = models.CharField(max_length=16)
    is_main_series = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pokedexes'


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    species = models.ForeignKey('PokemonSpecies', blank=True, null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.BooleanField()

    def __unicode__(self):
        return u'%s' % self.species.names.get(local_language__iso639='en').name

    class Meta:
        managed = False
        db_table = 'pokemon'


class PokemonAbilities(models.Model):
    pokemon = models.ForeignKey(Pokemon)
    ability = models.ForeignKey(Abilities)
    is_hidden = models.BooleanField()
    slot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_abilities'


class PokemonColorNames(models.Model):
    pokemon_color = models.ForeignKey('PokemonColors')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pokemon_color_names'


class PokemonColors(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pokemon_colors'


class PokemonDexNumbers(models.Model):
    species = models.ForeignKey('PokemonSpecies')
    pokedex = models.ForeignKey(Pokedexes)
    pokedex_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_dex_numbers'


class PokemonEggGroups(models.Model):
    species = models.ForeignKey('PokemonSpecies')
    egg_group = models.ForeignKey(EggGroups)

    class Meta:
        managed = False
        db_table = 'pokemon_egg_groups'


class PokemonEvolution(models.Model):
    id = models.IntegerField(primary_key=True)
    evolved_species = models.ForeignKey('PokemonSpecies',
                                        related_name='+')
    evolution_trigger = models.ForeignKey(EvolutionTriggers, related_name='+')
    trigger_item = models.ForeignKey(Items, blank=True, null=True)
    minimum_level = models.IntegerField(blank=True, null=True)
    gender = models.ForeignKey(Genders, blank=True, null=True)
    location = models.ForeignKey(Locations, blank=True, null=True)
    held_item = models.ForeignKey(Items, blank=True, null=True,
                                  related_name='+')
    time_of_day = models.TextField(blank=True,
                                   choices=(
                                       ('', 'Any time'),
                                       ('day', 'Day'),
                                       ('night', 'Night'),
                                   ))
    known_move = models.ForeignKey(Moves, blank=True, null=True)
    minimum_happiness = models.IntegerField(blank=True, null=True)
    minimum_beauty = models.IntegerField(blank=True, null=True)
    relative_physical_stats = models.IntegerField(blank=True, null=True)
    party_species = models.ForeignKey('PokemonSpecies', blank=True,
                                      null=True, related_name='+')
    trade_species = models.ForeignKey('PokemonSpecies', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_evolution'


class PokemonFormGenerations(models.Model):
    pokemon_form = models.ForeignKey('PokemonForms')
    generation = models.ForeignKey(Generations)
    game_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_form_generations'


class PokemonFormNames(models.Model):
    pokemon_form = models.ForeignKey('PokemonForms')
    local_language = models.ForeignKey(Languages)
    form_name = models.CharField(max_length=32, blank=True)
    pokemon_name = models.CharField(max_length=32, blank=True)

    class Meta:
        managed = False
        db_table = 'pokemon_form_names'


class PokemonFormPokeathlonStats(models.Model):
    pokemon_form = models.ForeignKey('PokemonForms')
    pokeathlon_stat = models.ForeignKey(PokeathlonStats)
    minimum_stat = models.IntegerField()
    base_stat = models.IntegerField()
    maximum_stat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_form_pokeathlon_stats'


class PokemonForms(models.Model):
    id = models.IntegerField(primary_key=True)
    form_identifier = models.CharField(max_length=16, blank=True)
    pokemon = models.ForeignKey(Pokemon)
    introduced_in_version_group = models.ForeignKey('VersionGroups', blank=True,
                                                    null=True)
    is_default = models.BooleanField()
    is_battle_only = models.BooleanField()
    form_order = models.IntegerField()
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_forms'


class PokemonGameIndices(models.Model):
    pokemon = models.ForeignKey(Pokemon)
    version = models.ForeignKey('Versions')
    game_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_game_indices'


class PokemonHabitatNames(models.Model):
    pokemon_habitat = models.ForeignKey('PokemonHabitats')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'pokemon_habitat_names'


class PokemonHabitats(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'pokemon_habitats'


class PokemonItems(models.Model):
    pokemon = models.ForeignKey(Pokemon)
    version = models.ForeignKey('Versions')
    item = models.ForeignKey(Items)
    rarity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_items'


class PokemonMoveMethodProse(models.Model):
    pokemon_move_method = models.ForeignKey('PokemonMoveMethods')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'pokemon_move_method_prose'


class PokemonMoveMethods(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'pokemon_move_methods'


class PokemonMoves(models.Model):
    pokemon = models.ForeignKey(Pokemon)
    version_group = models.ForeignKey('VersionGroups')
    move = models.ForeignKey(Moves)
    pokemon_move_method = models.ForeignKey(PokemonMoveMethods)
    level = models.IntegerField()
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_moves'


class PokemonShapeProse(models.Model):
    pokemon_shape = models.ForeignKey('PokemonShapes')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=24, blank=True)
    awesome_name = models.CharField(max_length=16, blank=True)

    class Meta:
        managed = False
        db_table = 'pokemon_shape_prose'


class PokemonShapes(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'pokemon_shapes'


class PokemonSpecies(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=20)
    generation = models.ForeignKey(Generations, blank=True, null=True)
    evolves_from_species = models.ForeignKey('self', blank=True, null=True)
    evolution_chain = models.ForeignKey(EvolutionChains, blank=True, null=True)
    color = models.ForeignKey(PokemonColors)
    shape = models.ForeignKey(PokemonShapes)
    habitat = models.ForeignKey(PokemonHabitats, blank=True, null=True)
    gender_rate = models.IntegerField()
    capture_rate = models.IntegerField()
    base_happiness = models.IntegerField()
    is_baby = models.BooleanField()
    hatch_counter = models.IntegerField()
    has_gender_differences = models.BooleanField()
    growth_rate = models.ForeignKey(GrowthRates)
    forms_switchable = models.BooleanField()
    order = models.IntegerField()
    conquest_order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.names.get(local_language__iso639='en').name

    class Meta:
        managed = False
        db_table = 'pokemon_species'


class PokemonSpeciesFlavorSummaries(models.Model):
    pokemon_species = models.ForeignKey(PokemonSpecies)
    local_language = models.ForeignKey(Languages)
    flavor_summary = models.CharField(max_length=512, blank=True)

    class Meta:
        managed = False
        db_table = 'pokemon_species_flavor_summaries'


class PokemonSpeciesFlavorText(models.Model):
    species = models.ForeignKey(PokemonSpecies)
    version = models.ForeignKey('Versions')
    language = models.ForeignKey(Languages)
    flavor_text = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pokemon_species_flavor_text'


class PokemonSpeciesNames(models.Model):
    pokemon_species = models.ForeignKey(PokemonSpecies, related_name='names',
                                        db_column='id')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=20, blank=True)
    genus = models.CharField(max_length=16, blank=True)

    class Meta:
        managed = False
        db_table = 'pokemon_species_names'


class PokemonSpeciesProse(models.Model):
    pokemon_species = models.ForeignKey(PokemonSpecies)
    local_language = models.ForeignKey(Languages)
    form_description = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'pokemon_species_prose'


class PokemonStats(models.Model):
    pokemon = models.ForeignKey(Pokemon)
    stat = models.ForeignKey('Stats')
    base_stat = models.IntegerField()
    effort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_stats'


class PokemonTypes(models.Model):
    pokemon = models.ForeignKey(Pokemon)
    type = models.ForeignKey('Types')
    slot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_types'


class RegionNames(models.Model):
    region = models.ForeignKey('Regions')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'region_names'


class Regions(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'regions'


class StatHintNames(models.Model):
    stat_hint = models.ForeignKey('StatHints')
    local_language = models.ForeignKey(Languages)
    message = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stat_hint_names'


class StatHints(models.Model):
    id = models.IntegerField(primary_key=True)
    stat = models.ForeignKey('Stats')
    gene_mod_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stat_hints'


class StatNames(models.Model):
    stat = models.ForeignKey('Stats')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'stat_names'


class Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    damage_class = models.ForeignKey(MoveDamageClasses, blank=True, null=True)
    identifier = models.CharField(max_length=16)
    is_battle_only = models.BooleanField()
    game_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stats'


class SuperContestCombos(models.Model):
    first_move = models.ForeignKey(Moves, related_name='+')
    second_move = models.ForeignKey(Moves)

    class Meta:
        managed = False
        db_table = 'super_contest_combos'


class SuperContestEffectProse(models.Model):
    super_contest_effect = models.ForeignKey('SuperContestEffects')
    local_language = models.ForeignKey(Languages)
    flavor_text = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'super_contest_effect_prose'


class SuperContestEffects(models.Model):
    id = models.IntegerField(primary_key=True)
    appeal = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'super_contest_effects'


class TypeEfficacy(models.Model):
    damage_type = models.ForeignKey('Types', related_name='+')
    target_type = models.ForeignKey('Types')
    damage_factor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'type_efficacy'


class TypeNames(models.Model):
    type = models.ForeignKey('Types')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'type_names'


class Types(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=12)
    generation = models.ForeignKey(Generations)
    damage_class = models.ForeignKey(MoveDamageClasses, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'


class VersionGroupPokemonMoveMethods(models.Model):
    version_group = models.ForeignKey('VersionGroups')
    pokemon_move_method = models.ForeignKey(PokemonMoveMethods)

    class Meta:
        managed = False
        db_table = 'version_group_pokemon_move_methods'


class VersionGroupRegions(models.Model):
    version_group = models.ForeignKey('VersionGroups')
    region = models.ForeignKey(Regions)

    class Meta:
        managed = False
        db_table = 'version_group_regions'


class VersionGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    generation = models.ForeignKey(Generations)
    pokedex = models.ForeignKey(Pokedexes, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version_groups'


class VersionNames(models.Model):
    version = models.ForeignKey('Versions')
    local_language = models.ForeignKey(Languages)
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'version_names'


class Versions(models.Model):
    id = models.IntegerField(primary_key=True)
    version_group = models.ForeignKey(VersionGroups)
    identifier = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'versions'
