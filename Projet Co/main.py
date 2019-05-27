import time
import Constants
import CalculMouv

Robot = CalculMouv.Control()

Robot.Toutfaire(3,3)

# #INITIALISATION POSITION
# POSITION_BASE = Constants.ANGLE_BASE_INIT
# POSITION_COUDE = Constants.ANGLE_COUDE_INIT
# POSITION_EPAULE = Constants.ANGLE_EPAULE_INIT
# POSITION_ROULIS = Constants.ANGLE_ROULIS_INIT
# POSITION_TANGAGE = Constants.ANGLE_TANGAGE_INIT
#
# #test en brut ligne i (1,2,3)
# ligne = 3
# # test en brut Colonne j (1,2,3)
# colonne = 3
#
# NumCase = Robot.Emplacement(ligne,colonne)
#
# angle_base = Robot.Calcul_Rotation_base(NumCase,POSITION_BASE,0,0)
# angle_coude = Robot.Calcul_Rotation_coude(NumCase,POSITION_COUDE,0,0)
# angle_epaule = Robot.Calcul_Rotation_epaule(NumCase,POSITION_EPAULE,0,0)
# angle_roulis = Robot.Calcul_Rotation_roulis(NumCase,POSITION_ROULIS,0,0)
# angle_tangage = Robot.Calcul_Rotation_tangage(NumCase,POSITION_TANGAGE,0,0)
#
# #Actualisation de la position du bras
# if angle_base != 0:
#     POSITION_BASE = POSITION_BASE + angle_base
# if angle_coude != 0:
#     POSITION_COUDE = POSITION_COUDE + angle_coude
# if angle_epaule != 0:
#     POSITION_EPAULE = POSITION_EPAULE + angle_epaule
# if angle_roulis != 0:
#     POSITION_ROULIS = POSITION_ROULIS + angle_roulis
# if angle_tangage != 0:
#     POSITION_TANGAGE = POSITION_TANGAGE + angle_tangage
#
# #Création des variables string pour la trame
#
# str_base = Robot.String_rotation(angle_base)
# str_coude = Robot.String_rotation(angle_coude)
# str_epaule = Robot.String_rotation(angle_epaule)
# str_roulis = Robot.String_rotation(angle_roulis)
# str_tangage = Robot.String_rotation(angle_tangage)
#
# #Trame de mouvement
#
# print('B:{0:s}.0:30 E:{1:s}.0:30 C:{2:s}.0:30 R:{3:s}.0:30 T:{4:s}.0:30'.format(
#     str_base,
#     str_epaule,
#     str_coude,
#     str_roulis,
#     str_tangage))
#
# #Position du bras
#
# print("Fin mouvement \n")
# print("Position du robot -> Base: {0:d}\nEpaule: {1:d}\nCoude: {2:d}\nRoulis: {3:d}\nTangage: {4:d}".format(
#     POSITION_BASE,
#     POSITION_EPAULE,
#     POSITION_COUDE,
#     POSITION_ROULIS,
#     POSITION_TANGAGE))
#
# time.sleep(5)
# print("Retour point d'approche..")
# time.sleep(1)
#
# #Retour point d'approche
#
# angle_base = Robot.Calcul_Rotation_base(NumCase,POSITION_BASE,1,0)
# angle_coude = Robot.Calcul_Rotation_coude(NumCase,POSITION_COUDE,1,0)
# angle_epaule = Robot.Calcul_Rotation_epaule(NumCase,POSITION_EPAULE,1,0)
# angle_roulis = Robot.Calcul_Rotation_roulis(NumCase,POSITION_ROULIS,1,0)
# angle_tangage = Robot.Calcul_Rotation_tangage(NumCase,POSITION_TANGAGE,1,0)
#
# #Actualisation de la position du bras
# if angle_base != 0:
#     POSITION_BASE = POSITION_BASE + angle_base
# if angle_coude != 0:
#     POSITION_COUDE = POSITION_COUDE + angle_coude
# if angle_epaule != 0:
#     POSITION_EPAULE = POSITION_EPAULE + angle_epaule
# if angle_roulis != 0:
#     POSITION_ROULIS = POSITION_ROULIS + angle_roulis
# if angle_tangage != 0:
#     POSITION_TANGAGE = POSITION_TANGAGE + angle_tangage
#
# #Création des variables string pour la trame
#
# str_base = Robot.String_rotation(angle_base)
# str_coude = Robot.String_rotation(angle_coude)
# str_epaule = Robot.String_rotation(angle_epaule)
# str_roulis = Robot.String_rotation(angle_roulis)
# str_tangage = Robot.String_rotation(angle_tangage)
#
# #Trame de mouvement
#
# print('B:{0:s}.0:30 E:{1:s}.0:30 C:{2:s}.0:30 R:{3:s}.0:30 T:{4:s}.0:30'.format(
#     str_base,
#     str_epaule,
#     str_coude,
#     str_roulis,
#     str_tangage))
#
# print("Fin mouvement \n")
# time.sleep(2)
#
# #Position du bras
#
# print("Position du robot -> Base: {0:d}\nEpaule: {1:d}\nCoude: {2:d}\nRoulis: {3:d}\nTangage: {4:d}".format(
#     POSITION_BASE,
#     POSITION_EPAULE,
#     POSITION_COUDE,
#     POSITION_ROULIS,
#     POSITION_TANGAGE))
