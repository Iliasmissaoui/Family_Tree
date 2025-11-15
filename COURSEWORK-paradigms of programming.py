#UPDATESD VERSION
class Person:
    def __init__(self, name, date_of_birth, date_of_death, parents=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.date_of_death = date_of_death
        self.parents = parents if parents else []

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_parents(self):
        return self.parents

    def get_age_at_death(self):
        if self.date_of_death and self.date_of_birth:
            return self.date_of_death - self.date_of_birth
        return None

    def get_children(self, family_tree):
        children = []
        for person in family_tree.values():
            if self.name in person.get_parents():
                children.append(person)
        return children


# F1 – Grandchildren
class GrandchildrenF1(Person):
    def get_grandchildren(self, family_tree):
        grandchildren = []
        for person in family_tree.values():
            for parent in person.get_parents():
                if parent in family_tree and self.name in family_tree[parent].get_parents():
                    grandchildren.append(person)
        return grandchildren


# F1 – Close Family
class CloseFamilyF1(Person):
    def __init__(self, name, date_of_birth, date_of_death, parents=None, spouse=None):
        super().__init__(name, date_of_birth, date_of_death, parents)
        self.spouse = spouse

    def get_close_family(self, family_tree):
        close_family = []

        # Parents
        parents = self.get_parents()
        for p in parents:
            if p in family_tree:
                close_family.append(family_tree[p])

        # Children
        for child in self.get_children(family_tree):
            close_family.append(child)

        # Siblings
        for person in family_tree.values():
            if person.name != self.name and set(person.get_parents()) == set(parents):
                close_family.append(person)

        # Spouse
        if self.spouse and self.spouse in family_tree:
            close_family.append(family_tree[self.spouse])

        return close_family


# F1 – Extended Family (Aunts, Uncles, Cousins)
def get_extended_family_F1(individual, family_tree):
    extended_family = []
    parents = individual.get_parents()

    # Loop through every person
    for person in family_tree.values():
        # Skip the individual
        if person.name == individual.name:
            continue

        # Their parents
        person_parents = person.get_parents()

        # Check if this person is an aunt/uncle (sibling of individual's parents)
        for parent in parents:
            if parent in person_parents:
                # Add aunt/uncle
                extended_family.append(person)

                # Add cousins (their children)
                for cousin in person.get_children(family_tree):
                    extended_family.append(cousin)

    return extended_family


# F2 – Siblings
class Siblings_F2(Person):
    def get_brothers_sisters(self, family_tree):
        siblings = []
        parents = set(self.get_parents())
        for person in family_tree.values():
            if person.name != self.name and set(person.get_parents()) == parents:
                siblings.append(person.name)
        return siblings


# F2 – Cousins
class Cousins_F2(Person):
    def get_cousins(self, family_tree):
        cousins = []
        parents = self.get_parents()

        for parent in parents:
            for person in family_tree.values():
                # Find siblings of parent (same grandparents)
                if parent in person.get_parents():
                    # Their children = cousins
                    for child in person.get_children(family_tree):
                        cousins.append(child.name)

        return cousins


# Birthday list
def birthday_list(family_tree):
    result = []
    for person in family_tree.values():
        result.append(f"{person.name} is born in {person.date_of_birth}")
    return result


# Sorted birthday list
def birthdays_sorter(family_tree):
    sortable = []
    for person in family_tree.values():
        sortable.append((person.date_of_birth, f"{person.name} is born in {person.date_of_birth}"))
    sortable.sort()
    return [text for _, text in sortable]


# F3A – Average age at death
def average_at_death(family_tree):
    total = 0
    count = 0
    for person in family_tree.values():
        age = person.get_age_at_death()
        if age is not None:
            total += age
            count += 1
    return total / count if count > 0 else 0


# F3A – Number of children
def get_n_of_children_for_person(person, family_tree):
    return len(person.get_children(family_tree))


# F3A – Average number of children
def average_of_children(family_tree):
    total_children = 0
    count_people = len(family_tree)

    for person in family_tree.values():
        total_children += len(person.get_children(family_tree))

    return total_children / count_people if count_people > 0 else 0


# ----------- FAMILY TREE DATA -----------

family_tree = {
    "david_emmersohn": Person("david_emmersohn", 1935, 2005),
    "lea_emmersohn": Person("lea_emmersohn", 1938, 2010),
    "john_smith": Person("john_smith", 1940, 2020),
    "rita_smith": Person("rita_smith", 1945, None),
    "otto_emmersohn": Person("otto_emmersohn", 1970, None, ["david_emmersohn", "lea_emmersohn"]),
    "emma_smith": Person("emma_smith", 1975, None, ["john_smith", "rita_smith"]),
    "ebi_emmersohn": Person("ebi_emmersohn", 1995, None, ["otto_emmersohn", "emma_smith"]),
    "aya_madloum": Person("aya_madloum", 1997, None),
    "liza_emmersohn": Person("liza_emmersohn", 1998, None, ["otto_emmersohn", "emma_smith"]),
    "abdo_mancini": Person("abdo_mancini", 1996, None),
    "nadia_emmersohn": Person("nadia_emmersohn", 2020, None, ["ebi_emmersohn", "aya_madloum"]),
    "yasmin_emmersohn": Person("yasmin_emmersohn", 2023, None, ["ebi_emmersohn", "aya_madloum"]),
    "dino_mancini": Person("dino_mancini", 2025, None, ["liza_emmersohn", "abdo_mancini"]),
    "cornelia": Person("cornelia", 1978, None, ["ana", "roy"]),
    "ana": Person("ana", 1950, 2024),
    "roy": Person("roy", 1948, None),
    "rania": Person("rania", 1982, None, ["ana", "roy"]),
    "rio": Person("rio", 1979, None),
    "arjo": Person("arjo", 2012, None, ["otto_emmersohn", "cornelia"]),
    "leila": Person("leila", 2009, None, ["otto_emmersohn", "cornelia"]),
    "sam": Person("sam", 2005, None, ["rio", "rania"]),
    "aya": Person("aya", 2003, None, ["rio", "rania"])
}

# ----------- TESTING -----------

# Average number of children
print("Average Number of Children per Person:", average_of_children(family_tree))

# Test date of birth
print("DOB for david_emmersohn:", family_tree["david_emmersohn"].get_date_of_birth())

# Test parents
print("Parents of otto:", family_tree["otto_emmersohn"].get_parents())

# Grandchildren
g = GrandchildrenF1("david_emmersohn", 1935, 2005).get_grandchildren(family_tree)
print("Grandchildren of David:", [x.name for x in g])

# Close family
otto_cf = CloseFamilyF1("otto_emmersohn", 1970, None, ["david_emmersohn", "lea_emmersohn"])
print("Close family of otto:", [x.name for x in otto_cf.get_close_family(family_tree)])

# Extended family
ext = get_extended_family_F1(family_tree["liza_emmersohn"], family_tree)
print("Extended family of Liza:", [x.name for x in ext])

# Average age at death
print("Average Age at Death:", average_at_death(family_tree))

# Siblings F2
leila = Siblings_F2("leila", 2009, None, ["otto_emmersohn", "cornelia"])
print("Siblings of leila:", leila.get_brothers_sisters(family_tree))
