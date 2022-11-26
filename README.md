# gamairoot-ce
GAMAI is Generalized and Applied Management of Academic Institutions - (Gestion Généralisée et Appliquée des Etablissements Universitaires)

GAMAI est une application developpée en Python permettant la gestion éfficace des scolarités et des enseignements au sein des Universités ou tout établissement de l'enseignement supérieur.

Modules gérés:

1** Gestion des inscriptions :
   -- Préinscription (Saisie des dossiers, Importation/Exportation des dossiers),
   -- Inscription administrative,
   -- Inscription académique,
   -- Gestion de paiements des frais universitaites
   Quelques états du module Gestion des inscriptions:
     .. Liste des étudiants préinscrits/inscrits (Par nationalité, par tranche d'age, par sexe, par région d'origine ...),
     .. Liste des étudiants avec situation de paiement des frais universitaires (insolvable et confirmer),
     .. Liste des étudiants inscrits par matière/Unité d'enseignement/Recapitulatif sur le programme,
     .. Importation/Exportation des etudiants inscrits,
  
2** Gestion des examens:
   -- Saisies et importations des notes d'évaluation (Examen, controle continu, travaux pratique ....), 
   -- Traitement des notes sous anonymats (Saisie des anonymats et importation/exportation)
   -- Importation/Exportation des notes (Examen, Control Continu, Travaux pratique ...)
   -- Définission des Jurys d'examens et affection par session
   Quelques états du module Gestion des examens:
     .. Procès verbal des notes par matières
     .. Procès verbal des notes par unité d'enseignement
     .. Procès verbal des notes par session et programme
     .. Procès verbal de synthèse des notes par semestre et par année académique
     .. Etat de saisie des notes par evaluation
     .. Etat de saisie des anonymats
     .. Etat des jurys d'examens
     
3** Administration:
   -- Gestion du système de notation (Notes sur 4, 20, 80, 100 ....),
   -- Definition des programmes de formation,
   -- Programmation des matières aux examens,
   -- Adoption des programmes de formation,
   -- Définission des périodes de traitements des notes,
   -- Attribution des matières aux enseignants,
   -- Traitement des années académiques, des sessions d'examens, des cursus de formation, des parcours, des semestres,
    Quelques états du module Administration:
     .. Etat des matières attribuées aux enseignants
     .. Etat des charges hauraires par enseignants
     .. Emploi de temps par periode/semestre
     
4** Gestion Système:
   -- Correction avancée des inscriptions des étudiants (Suppression, Migration ...),
   -- Fusion des doublons,
   -- Gestion multilangues du système (Ajout d'une nouvelle langue, choix de la langue par défaut, paramètres des documents multilangue ...),
   -- Paramétrage des positions sur les documents administratifs (Logo, Information de tutelle, signatiares, ...),
   -- Reconduction des paramètres
   Quelques états du module Gestion Système:
     .. Tableau de bord de verification des configurations de base
     .. Etat des corrections effectuées
     
5** Syncronisation: 
   -- Sauvegarde et restauration des Bases et données et applications
   -- Réparation des tables de la base de données
   -- Mises à jours de l'application et de la base de données

6** Production statistiques:
   -- Effectifs des inscrits/preinscrits par sexe, par region d'origine, par nationalité, par departement,
   -- Repartition par tranche d'age et par sexe,
   -- Repartion par région d'origine et par sexe,
   -- Repartion par pays d'origine et par sexe,
   -- Liste des étudiants étrangers par niveau, par option et par sexe,
   -- Liste des meilleurs étudiants par option/spécialité, par sexe, par pays d'origine, pour l'établissement, par département et par cursus,
   -- Taux de réussite par option/spécialité, par sexe, par pays d'origine, pour l'établissement, par département et par cursus,
   -- Evolution des inscriptions/préinscription par année, par spécialité, par sexe, pour l'établissement, par département et par cursus,
   -- Base de données de diplomés aux format Excel,
   -- Liste des étudiants par diplome d'admission
     
7** Gestion disciplinaire:
   -- Saisie des sanctions disciplinaire
   -- Application des sanctions disciplinaire
   -- Restauration des sanctions disciplinaire
   Quelques états du module Gestion Système:
     .. Etat des étudiants sanctinnés par option/spécialité, par sexe, par niveau et par établissement
     .. Liste des sanctions disciplinaires
     
