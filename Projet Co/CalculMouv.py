from machine import UART
import Constants
import time
import pycom


class Control:

#INITIALISATION POSITION
    def __init__(self):
        self.POSITION_BASE = Constants.ANGLE_BASE_INIT
        self.POSITION_COUDE = Constants.ANGLE_COUDE_INIT
        self.POSITION_EPAULE = Constants.ANGLE_EPAULE_INIT
        self.POSITION_ROULIS = Constants.ANGLE_ROULIS_INIT
        self.POSITION_TANGAGE = Constants.ANGLE_TANGAGE_INIT

    def Toutfaire(self,ligne,colonne):

        NumCase = self.Emplacement(ligne,colonne)

# MOUVEMENT PRISE DE CUBE....

        angle_base = self.Calcul_Rotation_base(NumCase,self.POSITION_BASE,0,1)
        angle_coude = self.Calcul_Rotation_coude(NumCase,self.POSITION_COUDE,0,1)
        angle_epaule = self.Calcul_Rotation_epaule(NumCase,self.POSITION_EPAULE,0,1)
        angle_roulis = self.Calcul_Rotation_roulis(NumCase,self.POSITION_ROULIS,0,1)
        angle_tangage = self.Calcul_Rotation_tangage(NumCase,self.POSITION_TANGAGE,0,1)

#Actualisation de la position du bras

        self.ActualisationPosition(angle_base,angle_coude,angle_epaule,angle_roulis,angle_tangage)

#Création des variables string pour la trame

        self.CreationTrame(angle_base,angle_coude,angle_epaule,angle_roulis,angle_tangage)

#Fermeture PINCE

        self.TrameFermeturePince()

# MOUVEMENT POINT D'APPROCHE

        angle_base = self.Calcul_Rotation_base(NumCase,self.POSITION_BASE,1,0)
        angle_coude = self.Calcul_Rotation_coude(NumCase,self.POSITION_COUDE,1,0)
        angle_epaule = self.Calcul_Rotation_epaule(NumCase,self.POSITION_EPAULE,1,0)
        angle_roulis = self.Calcul_Rotation_roulis(NumCase,self.POSITION_ROULIS,1,0)
        angle_tangage = self.Calcul_Rotation_tangage(NumCase,self.POSITION_TANGAGE,1,0)

#Actualisation de la position du bras

        self.ActualisationPosition(angle_base,angle_coude,angle_epaule,angle_roulis,angle_tangage)

#Création des variables string pour la trame

        self.CreationTrame(angle_base,angle_coude,angle_epaule,angle_roulis,angle_tangage)

# MOUVEMENT CASE PLATEAU

        angle_base = self.Calcul_Rotation_base(NumCase,self.POSITION_BASE,0,0)
        angle_coude = self.Calcul_Rotation_coude(NumCase,self.POSITION_COUDE,0,0)
        angle_epaule = self.Calcul_Rotation_epaule(NumCase,self.POSITION_EPAULE,0,0)
        angle_roulis = self.Calcul_Rotation_roulis(NumCase,self.POSITION_ROULIS,0,0)
        angle_tangage = self.Calcul_Rotation_tangage(NumCase,self.POSITION_TANGAGE,0,0)

#Actualisation de la position du bras

        self.ActualisationPosition(angle_base,angle_coude,angle_epaule,angle_roulis,angle_tangage)

#Création des variables string pour la trame

        self.CreationTrame(angle_base,angle_coude,angle_epaule,angle_roulis,angle_tangage)

#Ouverture PINCE

        self.TrameOuverturePince()

#RETOUR POINT D'APPROCHE

        angle_base = self.Calcul_Rotation_base(NumCase,self.POSITION_BASE,1,0)
        angle_coude = self.Calcul_Rotation_coude(NumCase,self.POSITION_COUDE,1,0)
        angle_epaule = self.Calcul_Rotation_epaule(NumCase,self.POSITION_EPAULE,1,0)
        angle_roulis = self.Calcul_Rotation_roulis(NumCase,self.POSITION_ROULIS,1,0)
        angle_tangage = self.Calcul_Rotation_tangage(NumCase,self.POSITION_TANGAGE,1,0)

#Actualisation de la position du bras

        self.ActualisationPosition(angle_base,angle_coude,angle_epaule,angle_roulis,angle_tangage)

#Création des variables string pour la trame

        self.CreationTrame(angle_base,angle_coude,angle_epaule,angle_roulis,angle_tangage)

        print("AU TOUR DU JOUEUR\n")


    def TrameOuverturePince(self):

        time.sleep(5)
        print('P:-200:02\n')


    def TrameFermeturePince(self):

        time.sleep(5)
        print('P:+200:02\n')



    def CreationTrame(self,base,coude,epaule,roulis,tangage):

        str_base = self.String_rotation(base)
        str_coude = self.String_rotation(coude)
        str_epaule = self.String_rotation(epaule)
        str_roulis = self.String_rotation(roulis)
        str_tangage = self.String_rotation(tangage)

        print('B:{0:s}.0:30 E:{1:s}.0:30 C:{2:s}.0:30 R:{3:s}.0:30 T:{4:s}.0:30\n'.format(
            str_base,
            str_epaule,
            str_coude,
            str_roulis,
            str_tangage))

        print("Fin mouvement \n")
        print("Position du robot -> Base: {0:d}\nEpaule: {1:d}\nCoude: {2:d}\nRoulis: {3:d}\nTangage: {4:d}".format(
            self.POSITION_BASE,
            self.POSITION_EPAULE,
            self.POSITION_COUDE,
            self.POSITION_ROULIS,
            self.POSITION_TANGAGE))

        time.sleep(5)


    def ActualisationPosition(self,base,coude,epaule,roulis,tangage):

        if base != 0:
            self.POSITION_BASE = self.POSITION_BASE + base
        if coude != 0:
            self.POSITION_COUDE = self.POSITION_COUDE + coude
        if epaule != 0:
            self.POSITION_EPAULE = self.POSITION_EPAULE + epaule
        if roulis != 0:
            self.POSITION_ROULIS = self.POSITION_ROULIS + roulis
        if tangage != 0:
            self.POSITION_TANGAGE = self.POSITION_TANGAGE + tangage

# Calcul de la case dans laquel le robot doit mettre le cube
# Voir modèle de répresentation plateau dans le rapport
    def Emplacement(self,ligne,colonne):
        self.emplacement = ligne*colonne
        if self.emplacement == 1 :
            self.Numcase = 1
        if self.emplacement == 2 :
            if colonne == 2 :
                self.Numcase = 2
            else:
                self.Numcase = 4
        if self.emplacement == 3:
            if colonne == 3:
                self.Numcase = 3
            else:
                self.Numcase = 7
        if self.emplacement == 4:
            self.Numcase = 5
        if self.emplacement == 6:
            if colonne == 3:
                self.Numcase = 6
            else:
                self.Numcase = 8
        if self.emplacement == 9:
            self.Numcase = 9

        return self.Numcase

    #Calcul de la valeur de rotation angulaire de la base

    def Calcul_Rotation_base(self,numcase,base,APP,CUBE):
        if APP == 1:
            if base > Constants.ANGLE_BASE_APP:
                self.Rotation = -1*abs(Constants.ANGLE_BASE_APP - base)
            else:
                self.Rotation = abs(Constants.ANGLE_BASE_APP - base)
            return self.Rotation
        if CUBE == 1:
            if base > Constants.ANGLE_BASE_CUBE:
                self.Rotation = -1*abs(Constants.ANGLE_BASE_CUBE - base)
            else:
                self.Rotation = abs(Constants.ANGLE_BASE_CUBE - base)
            return self.Rotation

        if numcase == 9:
            if base > Constants.ANGLE_BASE_9:
                self.Rotation = -1*abs(Constants.ANGLE_BASE_9 - base)
            else:
                self.Rotation = abs(Constants.ANGLE_BASE_9 - base)
        if numcase == 8:
            if base > Constants.ANGLE_BASE_8:
                self.Rotation = -1*abs(Constants.ANGLE_BASE_8 - base)
            else:
                self.Rotation = abs(Constants.ANGLE_BASE_8 - base)
        if numcase == 7:
            if base > Constants.ANGLE_BASE_7:
                self.Rotation = -1*abs(Constants.ANGLE_BASE_7 - base)
            else:
                self.Rotation = abs(Constants.ANGLE_BASE_7 - base)
        if numcase == 6:
            if base > Constants.ANGLE_BASE_6:
                self.Rotation = -1*abs(Constants.ANGLE_BASE_6 - base)
            else:
                self.Rotation = abs(Constants.ANGLE_BASE_6 - base)
        if numcase == 5:
            if base > Constants.ANGLE_BASE_5:
                self.Rotation = -1*abs(Constants.ANGLE_BASE_5 - base)
            else:
                self.Rotation = abs(Constants.ANGLE_BASE_5 - base)
        if numcase == 4:
            if base > Constants.ANGLE_BASE_4:
                self.Rotation = -1*abs(Constants.ANGLE_BASE_4 - base)
            else:
                self.Rotation = abs(Constants.ANGLE_BASE_4 - base)
        if numcase == 3:
            if base > Constants.ANGLE_BASE_3:
                self.Rotation = -1*abs(Constants.ANGLE_BASE_3 - base)
            else:
                self.Rotation = abs(Constants.ANGLE_BASE_3 - base)
        if numcase == 2:
            if base > Constants.ANGLE_BASE_2:
                self.Rotation = -1*abs(Constants.ANGLE_BASE_2 - base)
            else:
                self.Rotation = abs(Constants.ANGLE_BASE_2 - base)
        if numcase == 1:
            if base > Constants.ANGLE_BASE_1:
                self.Rotation = -1*abs(Constants.ANGLE_BASE_1 - base)
            else:
                self.Rotation = abs(Constants.ANGLE_BASE_1 - base)

        return self.Rotation

    #Calcul de la valeur de rotation angulaire du coude

    def Calcul_Rotation_coude(self,numcase,coude,APP,CUBE):
        if APP == 1:
            if coude > Constants.ANGLE_COUDE_APP:
                self.Rotation = -1*abs(Constants.ANGLE_COUDE_APP - coude)
            else:
                self.Rotation = abs(Constants.ANGLE_COUDE_APP - coude)
            return self.Rotation
        if CUBE == 1:
            if coude > Constants.ANGLE_COUDE_CUBE:
                self.Rotation = -1*abs(Constants.ANGLE_COUDE_CUBE - coude)
            else:
                self.Rotation = abs(Constants.ANGLE_COUDE_CUBE - coude)
            return self.Rotation

        if numcase == 9:
            if coude > Constants.ANGLE_COUDE_9:
                self.Rotation = -1*abs(Constants.ANGLE_COUDE_9 - coude)
            else:
                self.Rotation = abs(Constants.ANGLE_COUDE_9 - coude)
        if numcase == 8:
            if coude > Constants.ANGLE_COUDE_8:
                self.Rotation = -1*abs(Constants.ANGLE_COUDE_8 - coude)
            else:
                self.Rotation = abs(Constants.ANGLE_COUDE_8 - coude)
        if numcase == 7:
            if coude > Constants.ANGLE_COUDE_7:
                self.Rotation = -1*abs(Constants.ANGLE_COUDE_7 - coude)
            else:
                self.Rotation = abs(Constants.ANGLE_COUDE_7 - coude)
        if numcase == 6:
            if coude > Constants.ANGLE_COUDE_6:
                self.Rotation = -1*abs(Constants.ANGLE_COUDE_6 - coude)
            else:
                self.Rotation = abs(Constants.ANGLE_COUDE_6 - coude)
        if numcase == 5:
            if coude > Constants.ANGLE_COUDE_5:
                self.Rotation = -1*abs(Constants.ANGLE_COUDE_5 - coude)
            else:
                self.Rotation = abs(Constants.ANGLE_COUDE_5 - coude)
        if numcase == 4:
            if coude > Constants.ANGLE_COUDE_4:
                self.Rotation = -1*abs(Constants.ANGLE_COUDE_4 - coude)
            else:
                self.Rotation = abs(Constants.ANGLE_COUDE_4 - coude)
        if numcase == 3:
            if coude > Constants.ANGLE_COUDE_3:
                self.Rotation = -1*abs(Constants.ANGLE_COUDE_3 - coude)
            else:
                self.Rotation = abs(Constants.ANGLE_COUDE_3 - coude)
        if numcase == 2:
            if coude > Constants.ANGLE_COUDE_2:
                self.Rotation = -1*abs(Constants.ANGLE_COUDE_2 - coude)
            else:
                self.Rotation = abs(Constants.ANGLE_COUDE_2 - coude)
        if numcase == 1:
            if coude > Constants.ANGLE_COUDE_1:
                self.Rotation = -1*abs(Constants.ANGLE_COUDE_1 - coude)
            else:
                self.Rotation = abs(Constants.ANGLE_COUDE_1 - coude)

        return self.Rotation

    #Calcul de la valeur de rotation angulaire de l'épaule

    def Calcul_Rotation_epaule(self,numcase,epaule,APP,CUBE):
        if APP == 1:
            if epaule > Constants.ANGLE_EPAULE_APP:
                self.Rotation = -1*abs(Constants.ANGLE_EPAULE_APP - epaule)
            else:
                self.Rotation = abs(Constants.ANGLE_EPAULE_APP - epaule)
            return self.Rotation
        if CUBE == 1:
            if epaule > Constants.ANGLE_EPAULE_CUBE:
                self.Rotation = -1*abs(Constants.ANGLE_EPAULE_CUBE - epaule)
            else:
                self.Rotation = abs(Constants.ANGLE_EPAULE_CUBE - epaule)
            return self.Rotation

        if numcase == 9:
            if epaule > Constants.ANGLE_EPAULE_9:
                self.Rotation = -1*abs(Constants.ANGLE_EPAULE_9 - epaule)
            else:
                self.Rotation = abs(Constants.ANGLE_EPAULE_9 - epaule)
        if numcase == 8:
            if epaule > Constants.ANGLE_EPAULE_8:
                self.Rotation = -1*abs(Constants.ANGLE_EPAULE_8 - epaule)
            else:
                self.Rotation = abs(Constants.ANGLE_EPAULE_8 - epaule)
        if numcase == 7:
            if epaule > Constants.ANGLE_EPAULE_7:
                self.Rotation = -1*abs(Constants.ANGLE_EPAULE_7 - epaule)
            else:
                self.Rotation = abs(Constants.ANGLE_EPAULE_7 - epaule)
        if numcase == 6:
            if epaule > Constants.ANGLE_EPAULE_6:
                self.Rotation = -1*abs(Constants.ANGLE_EPAULE_6 - epaule)
            else:
                self.Rotation = abs(Constants.ANGLE_EPAULE_6 - epaule)
        if numcase == 5:
            if epaule > Constants.ANGLE_EPAULE_5:
                self.Rotation = -1*abs(Constants.ANGLE_EPAULE_5 - epaule)
            else:
                self.Rotation = abs(Constants.ANGLE_EPAULE_5 - epaule)
        if numcase == 4:
            if epaule > Constants.ANGLE_EPAULE_4:
                self.Rotation = -1*abs(Constants.ANGLE_EPAULE_4 - epaule)
            else:
                self.Rotation = abs(Constants.ANGLE_EPAULE_4 - epaule)
        if numcase == 3:
            if epaule > Constants.ANGLE_EPAULE_3:
                self.Rotation = -1*abs(Constants.ANGLE_EPAULE_3 - epaule)
            else:
                self.Rotation = abs(Constants.ANGLE_EPAULE_3 - epaule)
        if numcase == 2:
            if epaule > Constants.ANGLE_EPAULE_2:
                self.Rotation = -1*abs(Constants.ANGLE_EPAULE_2 - epaule)
            else:
                self.Rotation = abs(Constants.ANGLE_EPAULE_2 - epaule)
        if numcase == 1:
            if epaule > Constants.ANGLE_EPAULE_1:
                self.Rotation = -1*abs(Constants.ANGLE_EPAULE_1 - epaule)
            else:
                self.Rotation = abs(Constants.ANGLE_EPAULE_1 - epaule)

        return self.Rotation

    #Calcul de la valeur de rotation angulaire du roulis

    def Calcul_Rotation_roulis(self,numcase,roulis,APP,CUBE):
        if APP == 1:
            if roulis > Constants.ANGLE_ROULIS_APP:
                self.Rotation = -1*abs(Constants.ANGLE_ROULIS_APP - roulis)
            else:
                self.Rotation = abs(Constants.ANGLE_ROULIS_APP - roulis)
            return self.Rotation

        if CUBE == 1:
            if roulis > Constants.ANGLE_ROULIS_CUBE:
                self.Rotation = -1*abs(Constants.ANGLE_ROULIS_CUBE - roulis)
            else:
                self.Rotation = abs(Constants.ANGLE_ROULIS_CUBE - roulis)
            return self.Rotation


        if numcase == 9:
            if roulis > Constants.ANGLE_ROULIS_9:
                self.Rotation = -1*abs(Constants.ANGLE_ROULIS_9 - roulis)
            else:
                self.Rotation = abs(Constants.ANGLE_ROULIS_9 - roulis)
        if numcase == 8:
            if roulis > Constants.ANGLE_ROULIS_8:
                self.Rotation = -1*abs(Constants.ANGLE_ROULIS_8 - roulis)
            else:
                self.Rotation = abs(Constants.ANGLE_ROULIS_8 - roulis)
        if numcase == 7:
            if roulis > Constants.ANGLE_ROULIS_7:
                self.Rotation = -1*abs(Constants.ANGLE_ROULIS_7 - roulis)
            else:
                self.Rotation = abs(Constants.ANGLE_ROULIS_7 - roulis)
        if numcase == 6:
            if roulis > Constants.ANGLE_ROULIS_6:
                self.Rotation = -1*abs(Constants.ANGLE_ROULIS_6 - roulis)
            else:
                self.Rotation = abs(Constants.ANGLE_ROULIS_6 - roulis)
        if numcase == 5:
            if roulis > Constants.ANGLE_ROULIS_5:
                self.Rotation = -1*abs(Constants.ANGLE_ROULIS_5 - roulis)
            else:
                self.Rotation = abs(Constants.ANGLE_ROULIS_5 - roulis)
        if numcase == 4:
            if roulis > Constants.ANGLE_ROULIS_4:
                self.Rotation = -1*abs(Constants.ANGLE_ROULIS_4 - roulis)
            else:
                self.Rotation = abs(Constants.ANGLE_ROULIS_4 - roulis)
        if numcase == 3:
            if roulis > Constants.ANGLE_ROULIS_3:
                self.Rotation = -1*abs(Constants.ANGLE_ROULIS_3 - roulis)
            else:
                self.Rotation = abs(Constants.ANGLE_ROULIS_3 - roulis)
        if numcase == 2:
            if roulis > Constants.ANGLE_ROULIS_2:
                self.Rotation = -1*abs(Constants.ANGLE_ROULIS_2 - roulis)
            else:
                self.Rotation = abs(Constants.ANGLE_ROULIS_2 - roulis)
        if numcase == 1:
            if roulis > Constants.ANGLE_ROULIS_1:
                self.Rotation = -1*abs(Constants.ANGLE_ROULIS_1 - roulis)
            else:
                self.Rotation = abs(Constants.ANGLE_ROULIS_1 - roulis)

        return self.Rotation

    #Calcul de la valeur de rotation angulaire du tangage

    def Calcul_Rotation_tangage(self,numcase,tangage,APP,CUBE):
        if APP == 1:
            if tangage > Constants.ANGLE_TANGAGE_APP:
                self.Rotation = -1*abs(Constants.ANGLE_TANGAGE_APP - tangage)
            else:
                self.Rotation = abs(Constants.ANGLE_TANGAGE_APP - tangage)
            return self.Rotation

        if CUBE == 1:
            if tangage > Constants.ANGLE_TANGAGE_CUBE:
                self.Rotation = -1*abs(Constants.ANGLE_TANGAGE_CUBE - tangage)
            else:
                self.Rotation = abs(Constants.ANGLE_TANGAGE_CUBE - tangage)
            return self.Rotation

        if numcase == 9:
            if tangage > Constants.ANGLE_TANGAGE_9:
                self.Rotation = -1*abs(Constants.ANGLE_TANGAGE_9 - tangage)
            else:
                self.Rotation = abs(Constants.ANGLE_TANGAGE_9 - tangage)
        if numcase == 8:
            if tangage > Constants.ANGLE_TANGAGE_8:
                self.Rotation = -1*abs(Constants.ANGLE_TANGAGE_8 - tangage)
            else:
                self.Rotation = abs(Constants.ANGLE_TANGAGE_8 - tangage)
        if numcase == 7:
            if tangage > Constants.ANGLE_TANGAGE_7:
                self.Rotation = -1*abs(Constants.ANGLE_TANGAGE_7 - tangage)
            else:
                self.Rotation = abs(Constants.ANGLE_TANGAGE_7 - tangage)
        if numcase == 6:
            if tangage > Constants.ANGLE_TANGAGE_6:
                self.Rotation = -1*abs(Constants.ANGLE_TANGAGE_6 - tangage)
            else:
                self.Rotation = abs(Constants.ANGLE_TANGAGE_6 - tangage)
        if numcase == 5:
            if tangage > Constants.ANGLE_TANGAGE_5:
                self.Rotation = -1*abs(Constants.ANGLE_TANGAGE_5 - tangage)
            else:
                self.Rotation = abs(Constants.ANGLE_TANGAGE_5 - tangage)
        if numcase == 4:
            if tangage > Constants.ANGLE_TANGAGE_4:
                self.Rotation = -1*abs(Constants.ANGLE_TANGAGE_4 - tangage)
            else:
                self.Rotation = abs(Constants.ANGLE_TANGAGE_4 - tangage)
        if numcase == 3:
            if tangage > Constants.ANGLE_TANGAGE_3:
                self.Rotation = -1*abs(Constants.ANGLE_TANGAGE_3 - tangage)
            else:
                self.Rotation = abs(Constants.ANGLE_TANGAGE_3 - tangage)
        if numcase == 2:
            if tangage > Constants.ANGLE_TANGAGE_2:
                self.Rotation = -1*abs(Constants.ANGLE_TANGAGE_2 - tangage)
            else:
                self.Rotation = abs(Constants.ANGLE_TANGAGE_2 - tangage)
        if numcase == 1:
            if tangage > Constants.ANGLE_TANGAGE_1:
                self.Rotation = -1*abs(Constants.ANGLE_TANGAGE_1 - tangage)
            else:
                self.Rotation = abs(Constants.ANGLE_TANGAGE_1 - tangage)

        return self.Rotation

    def String_rotation(self,angle):

        if angle < 0:
                rotation_str = str(angle)
        else:
                rotation_str = str(angle)
                rotation_str = "+" + rotation_str

        return rotation_str
