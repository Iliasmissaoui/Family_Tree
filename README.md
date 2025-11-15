# 🧬 Desktop Family Tree — Python OOP Project

This project is a **Python-based family tree system** built using object-oriented programming (OOP).  
It models real family relationships and provides algorithms to explore and analyse a genealogical dataset.

The system includes:
- Family member modelling (`Person` class)
- OOP inheritance for extended features
- Relationship detection (siblings, cousins, grandchildren, extended family)
- Statistics such as:
  - Average age at death
  - Average number of children
  - Birthday lists + chronological sorting
- A custom dataset representing a multi-generation family tree

---

## 🚀 Features

### **📌 Core OOP Structure**
- `Person` class with:
  - name  
  - birth year  
  - death year  
  - parents  
  - spouse (optional)  
- Methods to compute:
  - age at death  
  - children  
  - parents  

### 📌 Relationship Modules
- **GrandchildrenF1** — finds all grandchildren of a given person  
- **CloseFamilyF1** — returns parents, siblings, spouse, and children  
- **Cousins_F2** — finds cousins through parental sibling relationships  
- **Siblings_F2** — returns brothers and sisters  

### **📌 Family Analysis Tools**
- List all birthdays  
- Sort members by birthdate  
- Compute demographic insights:
  - Average age at death
  - Average number of children per person

---

## 🛠️ Technologies Used
- **Python 3**
- Object-Oriented Programming (classes, inheritance, method overriding)
- Dictionaries & lists for data structures
- Basic algorithms for traversing graph-like family relationships

