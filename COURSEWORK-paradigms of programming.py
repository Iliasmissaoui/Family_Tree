class Person:
    def __init__(self, name, date_of_birth, date_of_death, parents=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.date_of_death = date_of_death
        self.parents = parents if parents else []

    # I will retrieve the date of birth of each person
    def get_date_of_birth(self):
        return self.date_of_birth

    # here I will retrieve the parents
    def get_parents(self):
        return self.parents

    # this function I added it after I have done F3 so it will be easier for me
    def get_age_at_death(self):
        if self.date_of_death and self.date_of_birth:
            return self.date_of_death - self.date_of_birth
        return None

    # function to get children
    def get_children(self, family_tree):
        children = []
        for person in family_tree.values():
            if self.name in person.get_parents():
                children.append(person)
        return children


# first task of the feature 1
class GrandchildrenF1(Person):
    def get_grandchildren(self, family_tree):
        grandchildren = []
        for member_name, person in family_tree.items():
            parents = person.get_parents()
            for parent in parents:
                if parent in family_tree and self.name in family_tree[parent].get_parents():
                    grandchildren.append(person)
        return grandchildren


# for close family I decided to include the spouse, the parents, and the brothers and sisters
class CloseFamilyF1(Person):
    def __init__(self, name, date_of_birth, date_of_death, parents=None, spouse=None):
        super().__init__(name, date_of_birth, date_of_death, parents)
        self.spouse = spouse  # Retain the spouse attribute

    def get_close_family(self, family_tree):
        close_family = []

        # Add parents
        parents = self.get_parents()
        if parents:
            close_family.extend(parents)

        # Add children
        children = self.get_children(family_tree)  # Pass family_tree as an argument
        if children:
            close_family.extend(children)

        # Add siblings
        for member_name, person in family_tree.items():
            if person.get_parents() == parents and member_name != self.name:
                close_family.append(person)

        # Add spouse, if defined
        if self.spouse:
            close_family.append(self.spouse)

        return close_family


# in the extended family I decided to add cousins and aunts, uncles as well
def get_extended_family_F1(name, family_tree):
    extended_family = []
    parents = name.get_parents()  # Fixed: Add parentheses to call the method
    # so here I will try to retrieve the cousins
    for member, person in family_tree.items():
        # I will retrieve the uncles
        p = person.get_parents()
        if any(parent in p for parent in parents):  # Check if the person's parents are siblings of individual's parents
            # here I am adding the aunts and uncles
            extended_family.append(member)  # Add the aunt/uncle
            # Retrieve their children (cousins)
            cousins = person.get_children(family_tree)
            for cousin in cousins:  # Iterate through the children of aunts/uncles
                extended_family.append(cousin.name)

    return extended_family  # Return the final extended family list


# F2
class Siblings_F2(Person):
    def get_brothers_sisters(self, family_tree):
        # so here the function will go to the person given then it will retrive its parents then compare it to each object in the dictionary then the person having the
        # same parents will be stored in our list
        brothers_and_sisters = []  # Fixed typo in the variable name
        parents = self.get_parents()
        for member_name, person in family_tree.items():
            if person.get_parents() == parents and member_name != self.name:  # go to each one's parent but not the person
                brothers_and_sisters.append(member_name)  # Fixed undefined variable
        return brothers_and_sisters


# F2 cousins
class Cousins_F2(Person):
    def get_cousins(self, family_tree):
        cousins = []
        parents = self.get_parents()
        for parent in parents:
            for member_name, person in family_tree.items():
                # Find siblings of the parent
                if parent in person.get_parents():
                    # Add their children as cousins
                    for child_name, child_person in family_tree.items():
                        if person.name in child_person.get_parents():
                            cousins.append(child_name)
        return cousins


# list of birthdays
def birthday_list(family_tree):
    list_of_birthday = []
    for member, person in family_tree.items():
        birthday = person.get_date_of_birth()
        phrase = f"{person.name} is born in {birthday}"
        list_of_birthday.append(phrase)
    return list_of_birthday


# birthday list sorter
def birthdays_sorter(family_tree):
    list_of_birthday = []
    for member, person in family_tree.items():
        birthday = person.get_date_of_birth()
        phrase = f"{person.name} is born in {birthday}"
        list_of_birthday.append((birthday, phrase))  # Fixed: Include birthday for sorting
    list_of_birthday.sort()  # Sort based on the birthday
    return [phrase for _, phrase in list_of_birthday]  # Return only the phrases


# F3 A II
# that is the first task of F3
# In this task I have tried to calculate the average age by making a variable taking the sum of all the ages then dividing by the N of person
def average_at_death(family_tree):
    total_age = 0
    count = 0
    for person in family_tree.values():
        age_at_death = person.get_age_at_death()  # that is a method in Person class which will calculate the age of a person
        if age_at_death is not None:  # the age should be known
            # a loop over all the members
            total_age += age_at_death  # It will calculate the sum of the age of all the member fo the family
            count += 1  # after adding each member the counter is increasing
    return total_age / count if count > 0 else 0


# F3A III

# number of children
def get_n_of_children_for_person(person, family_tree):
    children = person.get_children(family_tree)
    print(member.nameperson.get_children(family_tree))
    return len(children)


# average of children
def average_of_children(family_tree):
    people = []  # a list to store all the people in the family
    n_of_people = 0  # a counter for the member in the family
    total_children = 0
    for mem, person in family_tree.items():  # a loop through all the members in the family
        people.append(person)
        n_of_people += 1  # Increment for each person (corrected this as well)
    for mem, person in family_tree.items():
        children = person.get_children(family_tree)  # Pass family_tree as argument
        total_children += len(children)
    return total_children / n_of_people if n_of_people > 0 else 0


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

# Average number of children
avg_children = average_of_children(family_tree)
print("Average Number of Children per Person:", avg_children)

# Test for date of birth
print("Date of Birth for 'david_emmersohn':", family_tree["david_emmersohn"].get_date_of_birth())

# Test for parents
print("Parents of 'otto_emmersohn':", family_tree["otto_emmersohn"].get_parents())

# Test for grandchildren
grandchildren = GrandchildrenF1("david_emmersohn", 1935, 2005).get_grandchildren(family_tree)
print("Grandchildren of 'david_emmersohn':", [grandchild.name for grandchild in grandchildren])

# Test for close family
# Use the CloseFamilyF1 class instead of get_close_family function
otto_close_family = CloseFamilyF1("otto_emmersohn", 1970, None, ["david_emmersohn", "lea_emmersohn"])
close_family = otto_close_family.get_close_family(family_tree)

# Print the result for close family
print([member.name if hasattr(member, "name") else member for member in close_family])

# Test for extended family
extended_family = get_extended_family_F1(family_tree["liza_emmersohn"], family_tree)
print([member.name if hasattr(member, "name") else member for member in extended_family])

# Test for average age at death
avg_age_at_death = average_at_death(family_tree)
print("Average Age at Death:", avg_age_at_death)

# Reprinting average children for clarity
avg_children = average_of_children(family_tree)
print("Average Number of Children per Person:", avg_children)


leila = Siblings_F2("leila", 2009, None, ["otto_emmersohn", "cornelia"])
siblings_of_leila = leila.get_brothers_sisters(family_tree)
print(siblings_of_leila)







