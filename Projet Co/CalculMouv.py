from machine import UART
from Constants import *
import time
import pycom


class Control:

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
            if base > ANGLE_BASE_APP:
                self.Rotation = -1*abs(ANGLE_BASE_APP - base)
            else:
                self.Rotation = abs(ANGLE_BASE_APP - base)
            return self.Rotation
        if CUBE == 1:
            if base > ANGLE_BASE_CUBE:
                self.Rotation = -1*abs(ANGLE_BASE_CUBE - base)
            else:
                self.Rotation = abs(ANGLE_BASE_CUBE - base)
            return self.Rotation

        if numcase == 9:
            if base > ANGLE_BASE_9:
                self.Rotation = -1*abs(ANGLE_BASE_9 - base)
            else:
                self.Rotation = abs(ANGLE_BASE_9 - base)
        if numcase == 8:
            if base > ANGLE_BASE_8:
                self.Rotation = -1*abs(ANGLE_BASE_8 - base)
            else:
                self.Rotation = abs(ANGLE_BASE_8 - base)
        if numcase == 7:
            if base > ANGLE_BASE_7:
                self.Rotation = -1*abs(ANGLE_BASE_7 - base)
            else:
                self.Rotation = abs(ANGLE_BASE_7 - base)
        if numcase == 6:
            if base > ANGLE_BASE_6:
                self.Rotation = -1*abs(ANGLE_BASE_6 - base)
            else:
                self.Rotation = abs(ANGLE_BASE_6 - base)
        if numcase == 5:
            if base > ANGLE_BASE_5:
                self.Rotation = -1*abs(ANGLE_BASE_5 - base)
            else:
                self.Rotation = abs(ANGLE_BASE_5 - base)
        if numcase == 4:
            if base > ANGLE_BASE_4:
                self.Rotation = -1*abs(ANGLE_BASE_4 - base)
            else:
                self.Rotation = abs(ANGLE_BASE_4 - base)
        if numcase == 3:
            if base > ANGLE_BASE_3:
                self.Rotation = -1*abs(ANGLE_BASE_3 - base)
            else:
                self.Rotation = abs(ANGLE_BASE_3 - base)
        if numcase == 2:
            if base > ANGLE_BASE_2:
                self.Rotation = -1*abs(ANGLE_BASE_2 - base)
            else:
                self.Rotation = abs(ANGLE_BASE_2 - base)
        if numcase == 1:
            if base > ANGLE_BASE_1:
                self.Rotation = -1*abs(ANGLE_BASE_1 - base)
            else:
                self.Rotation = abs(ANGLE_BASE_1 - base)

        return self.Rotation

    #Calcul de la valeur de rotation angulaire du coude

    def Calcul_Rotation_coude(self,numcase,coude,APP,CUBE):
        if APP == 1:
            if coude > ANGLE_COUDE_APP:
                self.Rotation = -1*abs(ANGLE_COUDE_APP - coude)
            else:
                self.Rotation = abs(ANGLE_COUDE_APP - coude)
            return self.Rotation
        if CUBE == 1:
            if coude > ANGLE_COUDE_CUBE:
                self.Rotation = -1*abs(ANGLE_COUDE_CUBE - coude)
            else:
                self.Rotation = abs(ANGLE_COUDE_CUBE - coude)
            return self.Rotation

        if numcase == 9:
            if coude > ANGLE_COUDE_9:
                self.Rotation = -1*abs(ANGLE_COUDE_9 - coude)
            else:
                self.Rotation = abs(ANGLE_COUDE_9 - coude)
        if numcase == 8:
            if coude > ANGLE_COUDE_8:
                self.Rotation = -1*abs(ANGLE_COUDE_8 - coude)
            else:
                self.Rotation = abs(ANGLE_COUDE_8 - coude)
        if numcase == 7:
            if coude > ANGLE_COUDE_7:
                self.Rotation = -1*abs(ANGLE_COUDE_7 - coude)
            else:
                self.Rotation = abs(ANGLE_COUDE_7 - coude)
        if numcase == 6:
            if coude > ANGLE_COUDE_6:
                self.Rotation = -1*abs(ANGLE_COUDE_6 - coude)
            else:
                self.Rotation = abs(ANGLE_COUDE_6 - coude)
        if numcase == 5:
            if coude > ANGLE_COUDE_5:
                self.Rotation = -1*abs(ANGLE_COUDE_5 - coude)
            else:
                self.Rotation = abs(ANGLE_COUDE_5 - coude)
        if numcase == 4:
            if coude > ANGLE_COUDE_4:
                self.Rotation = -1*abs(ANGLE_COUDE_4 - coude)
            else:
                self.Rotation = abs(ANGLE_COUDE_4 - coude)
        if numcase == 3:
            if coude > ANGLE_COUDE_3:
                self.Rotation = -1*abs(ANGLE_COUDE_3 - coude)
            else:
                self.Rotation = abs(ANGLE_COUDE_3 - coude)
        if numcase == 2:
            if coude > ANGLE_COUDE_2:
                self.Rotation = -1*abs(ANGLE_COUDE_2 - coude)
            else:
                self.Rotation = abs(ANGLE_COUDE_2 - coude)
        if numcase == 1:
            if coude > ANGLE_COUDE_1:
                self.Rotation = -1*abs(ANGLE_COUDE_1 - coude)
            else:
                self.Rotation = abs(ANGLE_COUDE_1 - coude)

        return self.Rotation

    #Calcul de la valeur de rotation angulaire de l'épaule

    def Calcul_Rotation_epaule(self,numcase,epaule,APP,CUBE):
        if APP == 1:
            if epaule > ANGLE_EPAULE_APP:
                self.Rotation = -1*abs(ANGLE_EPAULE_APP - epaule)
            else:
                self.Rotation = abs(ANGLE_EPAULE_APP - epaule)
            return self.Rotation
        if CUBE == 1:
            if epaule > ANGLE_EPAULE_CUBE:
                self.Rotation = -1*abs(ANGLE_EPAULE_CUBE - epaule)
            else:
                self.Rotation = abs(ANGLE_EPAULE_CUBE - epaule)
            return self.Rotation

        if numcase == 9:
            if epaule > ANGLE_EPAULE_9:
                self.Rotation = -1*abs(ANGLE_EPAULE_9 - epaule)
            else:
                self.Rotation = abs(ANGLE_EPAULE_9 - epaule)
        if numcase == 8:
            if epaule > ANGLE_EPAULE_8:
                self.Rotation = -1*abs(ANGLE_EPAULE_8 - epaule)
            else:
                self.Rotation = abs(ANGLE_EPAULE_8 - epaule)
        if numcase == 7:
            if epaule > ANGLE_EPAULE_7:
                self.Rotation = -1*abs(ANGLE_EPAULE_7 - epaule)
            else:
                self.Rotation = abs(ANGLE_EPAULE_7 - epaule)
        if numcase == 6:
            if epaule > ANGLE_EPAULE_6:
                self.Rotation = -1*abs(ANGLE_EPAULE_6 - epaule)
            else:
                self.Rotation = abs(ANGLE_EPAULE_6 - epaule)
        if numcase == 5:
            if epaule > ANGLE_EPAULE_5:
                self.Rotation = -1*abs(ANGLE_EPAULE_5 - epaule)
            else:
                self.Rotation = abs(ANGLE_EPAULE_5 - epaule)
        if numcase == 4:
            if epaule > ANGLE_EPAULE_4:
                self.Rotation = -1*abs(ANGLE_EPAULE_4 - epaule)
            else:
                self.Rotation = abs(ANGLE_EPAULE_4 - epaule)
        if numcase == 3:
            if epaule > ANGLE_EPAULE_3:
                self.Rotation = -1*abs(ANGLE_EPAULE_3 - epaule)
            else:
                self.Rotation = abs(ANGLE_EPAULE_3 - epaule)
        if numcase == 2:
            if epaule > ANGLE_EPAULE_2:
                self.Rotation = -1*abs(ANGLE_EPAULE_2 - epaule)
            else:
                self.Rotation = abs(ANGLE_EPAULE_2 - epaule)
        if numcase == 1:
            if epaule > ANGLE_EPAULE_1:
                self.Rotation = -1*abs(ANGLE_EPAULE_1 - epaule)
            else:
                self.Rotation = abs(ANGLE_EPAULE_1 - epaule)

        return self.Rotation

    #Calcul de la valeur de rotation angulaire du roulis

    def Calcul_Rotation_roulis(self,numcase,roulis,APP,CUBE):
        if APP == 1:
            if roulis > ANGLE_ROULIS_APP:
                self.Rotation = -1*abs(ANGLE_ROULIS_APP - roulis)
            else:
                self.Rotation = abs(ANGLE_ROULIS_APP - roulis)
            return self.Rotation

        if CUBE == 1:
            if roulis > ANGLE_ROULIS_CUBE:
                self.Rotation = -1*abs(ANGLE_ROULIS_CUBE - roulis)
            else:
                self.Rotation = abs(ANGLE_ROULIS_CUBE - roulis)
            return self.Rotation


        if numcase == 9:
            if roulis > ANGLE_ROULIS_9:
                self.Rotation = -1*abs(ANGLE_ROULIS_9 - roulis)
            else:
                self.Rotation = abs(ANGLE_ROULIS_9 - roulis)
        if numcase == 8:
            if roulis > ANGLE_ROULIS_8:
                self.Rotation = -1*abs(ANGLE_ROULIS_8 - roulis)
            else:
                self.Rotation = abs(ANGLE_ROULIS_8 - roulis)
        if numcase == 7:
            if roulis > ANGLE_ROULIS_7:
                self.Rotation = -1*abs(ANGLE_ROULIS_7 - roulis)
            else:
                self.Rotation = abs(ANGLE_ROULIS_7 - roulis)
        if numcase == 6:
            if roulis > ANGLE_ROULIS_6:
                self.Rotation = -1*abs(ANGLE_ROULIS_6 - roulis)
            else:
                self.Rotation = abs(ANGLE_ROULIS_6 - roulis)
        if numcase == 5:
            if roulis > ANGLE_ROULIS_5:
                self.Rotation = -1*abs(ANGLE_ROULIS_5 - roulis)
            else:
                self.Rotation = abs(ANGLE_ROULIS_5 - roulis)
        if numcase == 4:
            if roulis > ANGLE_ROULIS_4:
                self.Rotation = -1*abs(ANGLE_ROULIS_4 - roulis)
            else:
                self.Rotation = abs(ANGLE_ROULIS_4 - roulis)
        if numcase == 3:
            if roulis > ANGLE_ROULIS_3:
                self.Rotation = -1*abs(ANGLE_ROULIS_3 - roulis)
            else:
                self.Rotation = abs(ANGLE_ROULIS_3 - roulis)
        if numcase == 2:
            if roulis > ANGLE_ROULIS_2:
                self.Rotation = -1*abs(ANGLE_ROULIS_2 - roulis)
            else:
                self.Rotation = abs(ANGLE_ROULIS_2 - roulis)
        if numcase == 1:
            if roulis > ANGLE_ROULIS_1:
                self.Rotation = -1*abs(ANGLE_ROULIS_1 - roulis)
            else:
                self.Rotation = abs(ANGLE_ROULIS_1 - roulis)

        return self.Rotation

    #Calcul de la valeur de rotation angulaire du tangage

    def Calcul_Rotation_tangage(self,numcase,tangage,APP,CUBE):
        if APP == 1:
            if tangage > ANGLE_TANGAGE_APP:
                self.Rotation = -1*abs(ANGLE_TANGAGE_APP - tangage)
            else:
                self.Rotation = abs(ANGLE_TANGAGE_APP - tangage)
            return self.Rotation

        if CUBE == 1:
            if tangage > ANGLE_TANGAGE_CUBE:
                self.Rotation = -1*abs(ANGLE_TANGAGE_CUBE - tangage)
            else:
                self.Rotation = abs(ANGLE_TANGAGE_CUBE - tangage)
            return self.Rotation

        if numcase == 9:
            if tangage > ANGLE_TANGAGE_9:
                self.Rotation = -1*abs(ANGLE_TANGAGE_9 - tangage)
            else:
                self.Rotation = abs(ANGLE_TANGAGE_9 - tangage)
        if numcase == 8:
            if tangage > ANGLE_TANGAGE_8:
                self.Rotation = -1*abs(ANGLE_TANGAGE_8 - tangage)
            else:
                self.Rotation = abs(ANGLE_TANGAGE_8 - tangage)
        if numcase == 7:
            if tangage > ANGLE_TANGAGE_7:
                self.Rotation = -1*abs(ANGLE_TANGAGE_7 - tangage)
            else:
                self.Rotation = abs(ANGLE_TANGAGE_7 - tangage)
        if numcase == 6:
            if tangage > ANGLE_TANGAGE_6:
                self.Rotation = -1*abs(ANGLE_TANGAGE_6 - tangage)
            else:
                self.Rotation = abs(ANGLE_TANGAGE_6 - tangage)
        if numcase == 5:
            if tangage > ANGLE_TANGAGE_5:
                self.Rotation = -1*abs(ANGLE_TANGAGE_5 - tangage)
            else:
                self.Rotation = abs(ANGLE_TANGAGE_5 - tangage)
        if numcase == 4:
            if tangage > ANGLE_TANGAGE_4:
                self.Rotation = -1*abs(ANGLE_TANGAGE_4 - tangage)
            else:
                self.Rotation = abs(ANGLE_TANGAGE_4 - tangage)
        if numcase == 3:
            if tangage > ANGLE_TANGAGE_3:
                self.Rotation = -1*abs(ANGLE_TANGAGE_3 - tangage)
            else:
                self.Rotation = abs(ANGLE_TANGAGE_3 - tangage)
        if numcase == 2:
            if tangage > ANGLE_TANGAGE_2:
                self.Rotation = -1*abs(ANGLE_TANGAGE_2 - tangage)
            else:
                self.Rotation = abs(ANGLE_TANGAGE_2 - tangage)
        if numcase == 1:
            if tangage > ANGLE_TANGAGE_1:
                self.Rotation = -1*abs(ANGLE_TANGAGE_1 - tangage)
            else:
                self.Rotation = abs(ANGLE_TANGAGE_1 - tangage)

        return self.Rotation

    def String_rotation(self,angle):

        if angle < 0:
                rotation_str = str(angle)
        else:
                rotation_str = str(angle)
                rotation_str = "+" + rotation_str

        return rotation_str
