from datetime import datetime
from icalendar import Calendar, Event
import os
import requests
import sys

FILTER_OUT = [
    "Préparation TOEIC 4A",
    "Software Engineering & Design Principles TD2",
    # "Réunion Nouveaux Etudiants Internationaux",
    # "DSA - TP option 2",
    "MSST2",
    "DDRS - introduction",
    "Software Engineering & Design Principles CM",
    "Pol'Innov challenge - introduction (Amphi Dumontet)",
    "Entrepôts : 3.ETL G2",
    "IWA - CTD - option 2 - Ingénierie des Applications Web 2",
    # "AI & Multi-Agent Systems CM",
    "O2 - TILE - Traitement d'Information à Large Echelle",
    "Software Engineering & Design Principles TD1",
    "Finance d'entreprise CMTD1",
    "Pol'Innov challenge - jury",
    # "FP - TP option 2 - Programmation Fonctionnelle Faaiz",
    # "AI & Multi-Agent Systems TD1",
    "Statistical learning CMTD2",
    "O2 - TILE - EXAM Traitement d'Information à Large Echelle - Examen",
    "Algo avancée 1 CM",
    "IWA - TD option 1 - Ingénierie des Applications Web 2",
    # "Econométrie - Examen techniques de scoring",
    "IWA - CTD - option 1 - Ingénierie des Applications Web 2",
    "O1 - Audit des Systèmes d'Information (ASI) IA - mirka",
    "Simulation d'ent CM",
    # "Deep learning TP 2",
    # "Fond.du machine learning TP1",
    "Simulation d'ent TD2",
    "BdD distribuées et noSQL TD1",
    "CPO2 TD2",
    "O2 - CMS",
    "Entrepôts : 1.Modélisation  G1",
    "TSI - CM - Tests des Systèmes d'Information",
    # "Proj Data Science - Soutenances",
    "Software Engineering & Design Principles Examen",
    "BdD distribuées et noSQL TP2",
    "Management des SI Examen",
    "PR&D - CM",
    # "SSI - Sécurité des Systèmes d'Information-lucato",
    "Management des SI CMTD2",
    "Conférence handicap et insertion pro",
    "Simulation d'ent- Oral",
    "creation profil linkind IG5 option 1",
    "Réunion information entrepreneuriat - 4A",
    "PPRP - ESN, WTF ? @Viveris",
    "GP - TP option 1 - Gestion projets rectorat",
    # "SSI - Sécurité des Systèmes d'Information Michel facerias",
    "Forum Entreprise FISE 4A-5A",
    "TD option 1 -avant vente",
    "ID - EXAMEN Introduction au Droit",
    # "IA générative LLM CM",
    "Réunion de rentrée IG3 et IG4 - Amphi Peytavin",
    # "IA générative LLM TP1",
    # "Systèmes de recommandation CM",
    # "Fin des cours du S7",
    "Entrepôts : 2.Reporting G1",
    "Finance d'entreprise Examen",
    # "Deep learning TP 1",
    "Pol'Innov challenge - TD",
    "TSI - TP Tests des Systèmes d'Information",
    # "ScikitLearn Débutant",
    "Oraux Projet IWA",
    # "FP - TD option 2 - Programmation Fonctionnelle nouguier",
    # "Deep learning CM",
    "Algo avancée 1 CMTD1",
    # "AI & Multi-Agent Systems Examen",
    "GP - TP option 1 - Gestion projets-TDD",
    "Simulation d'ent TD1",
    "Algo avancée 1 CMTD2",
    "O1 - OSI - CM",
    # "IDO - TP - groupe 1",
    "Algo avancée 1 TD2",
    "O2 - Traitement de données temporelles",
    "CPO2 Examen",
    # "FP - CM - Programmation Fonctionnelle N. nouguier",
    "Espagnol G1",
    "ID - Introduction au Droit",
    # "Fond.du machine learning TP2",
    "PR&D - TD Option 1",
    "PR&D - TD Option 2",
    "O2 - RFID",
    "Software Engineering Practices CM",
    "GP - CM - Gestion de projets IA",
    "BdD distribuées et noSQL CM",
    # "Econométrie - CM - Polytech techniques de scoring",
    "Réunion de rentrée - contrats pros",
    "Pol'Innov challenge - conférence (amphi Dumontet)",
    # "Semaine Internationale - Global Village",
    # "Nuit de l'info",
    "BdD distribuées et noSQL TD2",
    "AWI CMTD1",
    # "FP - CM - Programmation Fonctionnelle Faaiz",
    "Software Engineering Practices TP1",
    # "TD O2 Econométrie techniques de scoring",
    "Réunion tutorat IG4/3",
    "O1 - Audit des Systèmes d'Information (ASI) 6h",
    "Anglais G2",
    # "Cohésion IG",
    "USI - Urbanisation des Systèmes d'Information",
    "Statistical learning Examen",
    "creation profil linkind IG5 option 2",
    # "FP - TD option 2 - Programmation Fonctionnelle Faaiz",
    "DDRS - restitution",
    # "DSA - TP option 1",
    # "FP - TD option 1 - Programmation FonctionnelleNouguier",
    "Algo avancée 1 Examen",
    "GP - CM - Gestion de projets rectorat",
    # "Systèmes de recommandation TP1",
    "Entrepôts : 3.ETL G1",
    "Entrepôts : 2.Reporting G2",
    "Pol'Innov Challenge - Clôture",
    "Réunion information entrepreneuriat - 5A",
    "Finance d'entreprise CM",
    "Entrepôts : 1.Modélisation G2",
    "Entrepôts Examen",
    # "Remise des diplômes (banalisation des cours)",
    "CPO2 TD1",
    "AI & Multi-Agent Systems CMTD2",
    "IWA - TD option 2 - Ingénierie des Applications Web 2",
    "O1 - OSI - Optimisation des Systèmes d'Information",
    "IWA - Proj option 2 - Autonomie",
    "Entrepôts : 1.Modélisation CM",
    # "Journées blanches",
    "Software Engineering Practices TP2",
    # "FP - TD option 1 - Programmation Fonctionnelle Faaiz",
    "Conseil pédagogique",
    "Pol'Innov challenge -  préparation jury",
    # "FP - TP option 1- Programmation Fonctionnelle Faaiz",
    "Algo avancée 1 TD1",
    # "Systèmes de recommandation TP2",
    "CPO2 CMTD2",
    "IWA - Proj option 1 - Autonomie",
    # "AI & Multi-Agent Systems CMTD1",
    # "Fond.du machine learning",
    "Entrepôts 2. Reporting et + CM",
    "Management des SI CMTD1",
    "Rentrée IG5",
    # "TD O1 - Econométrie techniques de scoring",
    "BdD distribuées et noSQL TP1",
    "DI - CM - propriété intellectuelle",
    "Statistical learning CMTD1",
    "Présentation Sujets PFE",
    "Finance d'entreprise CMTD2",
    # "IA générative LLM TP2",
    # "IDO - TP - groupe 2",
    "GP - CM - Gestion de projets- TDD BDD...",
    # "IDO - CMTD",
    "AWI CMTD2",
    "GP - TD option 1 - Gestion projets IA",
    # "AI & Multi-Agent Systems TD2",
    # "DSA - CM - Data science Avancée",
    # "SSI - Sécurité des Systèmes d'Information Hubert Grégoire",
    "O2 - RFID Exam",
    "Anglais G1",
    # "DI - CM - protection des données",
    "CPO2 CMTD1",
    "CM - avant vente",
    "Business models et Data",
    "BdD distribuées et noSQL Examen",
]

def fetch_calendar(url):
    response = requests.get(url)
    response.raise_for_status()
    return Calendar.from_ical(response.content)


def process_event(event):
    summary = str(event.get('summary', ''))

    if summary in FILTER_OUT:
        return None

    return event

def filter_calendar(calendar):
    result = Calendar()

    for component in calendar.walk():
        if component.name == "VEVENT":
            modified_event = process_event(component)
            if modified_event:
                result.add_component(modified_event)

        elif component.name == "VCALENDAR":
            pass

        else:
            result.add_component(component)

    return result


def main(calendar_url, output_path="cal.ics"):

    calendar = fetch_calendar(calendar_url)

    new_calendar = filter_calendar(calendar)

    with open(output_path, "wb") as f:
        f.write(new_calendar.to_ical())


if __name__ == "__main__":

    input_url = os.environ.get("CALENDAR_URL")
    output_path = os.environ.get("OUTPUT_PATH", "cal.ics")

    main(input_url, output_path)
