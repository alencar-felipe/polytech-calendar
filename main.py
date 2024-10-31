from icalendar import Calendar
import os
import requests

FILTER_OUT = [
    # "AI & Multi-Agent Systems CM",
    # "AI & Multi-Agent Systems CMTD1",
    # "AI & Multi-Agent Systems CMTD2",
    # "AI & Multi-Agent Systems Examen",
    # "AI & Multi-Agent Systems TD1",
    # "AI & Multi-Agent Systems TD2",
    "AWI CMTD1",
    "AWI CMTD1 Autonom",
    "AWI CMTD2",
    "AWI CMTD2 Autonom",
    "Algo avancée 1 CM",
    "Algo avancée 1 CMTD1",
    "Algo avancée 1 CMTD2",
    "Algo avancée 1 Examen",
    "Algo avancée 1 TD1",
    "Algo avancée 1 TD2",
    "Anglais G1",
    "Anglais G2",
    "ArchiCirc. Num 1",
    "Attribution projets S7",
    "BdD distribuées et noSQL CM",
    "BdD distribuées et noSQL Examen",
    "BdD distribuées et noSQL TD1",
    "BdD distribuées et noSQL TD2",
    "BdD distribuées et noSQL TP1",
    "BdD distribuées et noSQL TP2",
    "Business models et Data",
    "CIA 2",
    "CIA 2 : auto-formation",
    "CIA/CIN, Révision",
    "CIN 2",
    "CM - avant vente",
    "CPO2 CMTD1",
    "CPO2 CMTD2",
    "CPO2 Examen",
    "CPO2 TD1",
    "CPO2 TD2",
    # "Cohésion IG",
    "Conférence handicap et insertion pro",
    "Conseil pédagogique",
    "DDRS - Grp1",
    "DDRS - Grp2",
    "DDRS - Grp3",
    "DDRS - Grp4",
    "DDRS - introduction",
    "DDRS - restitution",
    # "DI - CM - propriété intellectuelle",
    # "DI - CM - protection des données",
    # "DSA - CM - Data science Avancée",
    # "DSA - TP option 1",
    # "DSA - TP option 2",
    # "Deep learning CM",
    # "Deep learning TP 1",
    # "Deep learning TP 2",
    # "Econométrie - CM - Polytech techniques de scoring",
    # "Econométrie - Examen techniques de scoring",
    "Entrepôts 2. Reporting et + CM",
    "Entrepôts : 1.Modélisation  G1",
    "Entrepôts : 1.Modélisation CM",
    "Entrepôts : 1.Modélisation G2",
    "Entrepôts : 2.Reporting G1",
    "Entrepôts : 2.Reporting G2",
    "Entrepôts : 3.ETL G1",
    "Entrepôts : 3.ETL G2",
    "Entrepôts Examen",
    "Exam ArchiCirc. Num 1",
    "Exam CIN 2",
    "Exam Modélisation 3D",
    "Exam syst OS TR",
    "FLE DDL S1",
    # "FP - CM - Programmation Fonctionnelle Faaiz",
    # "FP - CM - Programmation Fonctionnelle N. nouguier",
    # "FP - TD option 1 - Programmation Fonctionnelle Faaiz",
    # "FP - TD option 1 - Programmation FonctionnelleNouguier",
    # "FP - TD option 2 - Programmation Fonctionnelle Faaiz",
    # "FP - TD option 2 - Programmation Fonctionnelle nouguier",
    # "FP - TP option 1- Programmation Fonctionnelle Faaiz",
    # "FP - TP option 2 - Programmation Fonctionnelle Faaiz",
    "Filtrage et TNS",
    "Filtrage et TNS, Examen",
    "Filtrage et TNS, Tiers temps",
    # "Fin des cours du S7",
    "Finance d'entreprise CM",
    "Finance d'entreprise CMTD1",
    "Finance d'entreprise CMTD2",
    "Finance d'entreprise Examen",
    "Finance d'entreprise Examen 1",
    # "Fond.du machine learning",
    # "Fond.du machine learning TP1",
    # "Fond.du machine learning TP2",
    "Forum Entreprise FISE 4A-5A",
    "GP - CM - Gestion de projets IA",
    "GP - CM - Gestion de projets rectorat",
    "GP - CM - Gestion de projets- TDD BDD...",
    "GP - TD option 1 - Gestion projets IA",
    "GP - TP option 1 - Gestion projets rectorat",
    "GP - TP option 1 - Gestion projets-TDD",
    "Graphes et applications",
    "Graphes et applications, exam",
    # "IA générative LLM CM",
    # "IA générative LLM TP1",
    # "IA générative LLM TP2",
    "ID - EXAMEN Introduction au Droit",
    "ID - Introduction au Droit",
    # "IDO - CMTD",
    # "IDO - TP - groupe 1",
    # "IDO - TP - groupe 2",
    # "IWA - CTD - option 1 - Ingénierie des Applications Web 2",
    # "IWA - CTD - option 2 - Ingénierie des Applications Web 2",
    # "IWA - Proj option 1 - Autonomie",
    # "IWA - Proj option 2 - Autonomie",
    # "IWA - TD option 1 - Ingénierie des Applications Web 2",
    # "IWA - TD option 2 - Ingénierie des Applications Web 2",
    "Insertion Pro",
    # "Journées blanches",
    "MSST2",
    "Management des SI CMTD1",
    "Management des SI CMTD2",
    "Management des SI Examen",
    "Modulateurs",
    "Modulateurs, examen",
    "Modulateurs, tiers-temps",
    "Modélisation 3D",
    # "Nuit de l'info",
    # "O1 - Audit des Systèmes d'Information (ASI) 6h",
    # "O1 - Audit des Systèmes d'Information (ASI) IA - mirka",
    "O1 - OSI - CM",
    "O1 - OSI - Optimisation des Systèmes d'Information",
    "O2 - CMS",
    "O2 - RFID",
    "O2 - RFID Exam",
    "O2 - TILE - EXAM Traitement d'Information à Large Echelle - Examen",
    "O2 - TILE - Traitement d'Information à Large Echelle",
    "O2 - Traitement de données temporelles",
    "OS TR",
    # "Oraux Projet IWA",
    "Org & Fct Entreprises MEA4",
    "Org & Fct Entreprises, Tiers-temps",
    "POO & Modélisation (G1)",
    "POO & Modélisation (G2)",
    "POO & Modélisation (MEA)",
    "PPRP - ESN, WTF ? @Viveris",
    "PR&D - CM",
    "PR&D - TD Option 1",
    "PR&D - TD Option 2",
    # "Perception 1",
    # "Perception 1, Examen",
    # "Perception 1, tiers-temps",
    "Pol'Innov Challenge - Clôture (Amphi Dumontet)",
    "Pol'Innov challenge -  préparation jury",
    "Pol'Innov challenge - TD",
    "Pol'Innov challenge - conférence (amphi Dumontet)",
    "Pol'Innov challenge - introduction (Amphi Dumontet)",
    "Pol'Innov challenge - jury",
    # "Proj Data Science - Soutenances",
    "Projet S5, Soutenance",
    "Projet Transversal S7",
    "Projet de robotique S7",
    "Préparation TOEIC 4A",
    "Présentation Sujets PFE",
    # "Présentation partenaire académique UFRGS (Brésil)",
    # "Remise des diplômes (banalisation des cours)",
    "Rentrée IG5",
    "Rentrée MEA4 (SC001)",
    "Réseaux embarqués",
    "Réseaux embarqués, Examen",
    "Réseaux embarqués, tiers-temps",
    # "Réunion Nouveaux Etudiants Internationaux",
    "Réunion de rentrée - contrats pros",
    "Réunion de rentrée IG3 et IG4 - Amphi Peytavin",
    "Réunion information entrepreneuriat - 4A",
    "Réunion information entrepreneuriat - 5A",
    "Réunion tutorat IG4/3",
    # "SSI - Sécurité des Systèmes d'Information Hubert Grégoire",
    # "SSI - Sécurité des Systèmes d'Information Michel facerias",
    # "SSI - Sécurité des Systèmes d'Information-lucato",
    # "ScikitLearn Débutant",
    # "Semaine Internationale - Global Village",
    "Simulation d'ent CM",
    "Simulation d'ent TD1",
    "Simulation d'ent TD2",
    "Simulation d'ent- Oral",
    "Software Engineering & Design Principles CM",
    "Software Engineering & Design Principles Examen",
    "Software Engineering & Design Principles TD1",
    "Software Engineering & Design Principles TD2",
    "Software Engineering Practices CM",
    "Software Engineering Practices TP1",
    "Software Engineering Practices TP2",
    "Soutenances Projets S7",
    "Statistical learning CMTD1",
    "Statistical learning CMTD2",
    "Statistical learning Examen",
    "Sys. Lin. Multivariables",
    "Sys. lin. multivariable",
    "Sys.Lin.Multi.Var",
    "Sys.Lin.Multi.Var, Examen",
    "Sys.Lin.Multi.Var, tiers-temps",
    "Syst OS TR",
    # "Systèmes de recommandation CM",
    # "Systèmes de recommandation TP1",
    # "Systèmes de recommandation TP2",
    "T. analogique du signal",
    "T. analogique du signal (FM)",
    "T. analogique du signal (GC)",
    "T. analogique du signal, 1/3 temps",
    "T. analogique du signal, Examen",
    # "TD O1 - Econométrie techniques de scoring",
    # "TD O2 Econométrie techniques de scoring",
    "TD option 1 -avant vente",
    "TSI - CM - Tests des Systèmes d'Information",
    "TSI - TP Tests des Systèmes d'Information",
    "Tiers-temps ArchiCirc. Num 1",
    "Tiers-temps CIN 2",
    "Tiers-temps Modélisation 3D",
    "Tiers-temps syst OS TR",
    "USI - Urbanisation des Systèmes d'Information",
    "creation profil linkind IG5 option 1",
    "creation profil linkind IG5 option 2"
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
