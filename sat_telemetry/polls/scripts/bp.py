# -*- coding: utf-8 -*-
import numpy as np

import math


class Controle:
    PI=np.float64(3.1415926535898)
    PIV2=np.float64(PI + PI)
    RAD=PI / 180.0
    DEG=180.0 / PI

    def GDGCP(self, XGD):
        AE=np.float64(6378137.0)
        FLAT=np.float64(1.0 / 298.257223563)

        #      IMPLICIT REAL*8 (A-H,O-Z)
        AL=XGD[0]  # East longitude
        FI=XGD[1]  # Geodetic latitude
        H=XGD[2]  # Heigth

        SF=np.sin(FI)
        CF=np.cos(FI)
        GAMA=(1.0 - FLAT) ** 2
        S=AE / np.sqrt(1.0 - (1.0 - GAMA) * SF * SF)
        G1=S + H
        G2=S * GAMA + H

        XGC=np.zeros(3)

        XGC[0]=G1 * CF * np.cos(AL)
        XGC[1]=G1 * CF * np.sin(AL)
        XGC[2]=G2 * SF

        return XGC

    def GCTOP(self, XT, GEO):
        RT=np.float64(6378137.00)
        F=np.float64(1.0 / 298.2572235630)
        #
        SILO=np.sin(GEO[0])
        SILA=np.sin(GEO[1])
        COLO=np.cos(GEO[0])
        COLA=np.cos(GEO[1])
        AUXI=1 - F
        GAMA=AUXI * AUXI
        AUXI=RT / np.sqrt(1 - F * (2 - F) * SILA * SILA)
        #
        COSG=COLA * (AUXI + GEO[2])
        X=XT[0] - COSG * COLO
        Y=XT[1] - COSG * SILO
        Z=XT[2] - SILA * (GAMA * AUXI + GEO[2])

        xtop=np.zeros(3)

        COSG=X * COLO + Y * SILO
        xtop[0]=COSG * SILA - Z * COLA
        xtop[1]=Y * COLO - X * SILO
        xtop[2]=Z * SILA + COSG * COLA

        return xtop

    def TANGEN(self, SINO, COSI):
        tangen=np.float64(0)
        if SINO == 0 and COSI == 0:
            tangen=np.float64(0)
        else:
            tangen=np.float64(math.atan2(SINO, COSI))
            if tangen < 0.0:
                tangen=tangen + self.PIV2
        return tangen

    def TOTSP(self, xtop):
        xh=xtop[0]
        yh=xtop[1]
        zh=xtop[2]

        x2_y2=xh * xh + yh * yh
        ro=np.sqrt(x2_y2 + zh * zh)
        sih=zh / ro

        atop=np.zeros(3)
        atop[0]=self.TANGEN(yh, -xh)
        atop[1]=math.asin(sih)
        atop[2]=ro

        return atop

    def GCTSP(self, xt, geo):
        xtop=self.GCTOP(xt, geo)
        atop=self.TOTSP(xtop)

        return atop

    def balloon_gps_receiver_pointing(self, vgps, vsta):
        xgd=np.zeros(3)
        geo=np.zeros(3)
        v_bpa=np.zeros(3)
        # Transforming from Geodetic spheric to Geocentric rectangular coordinates
        xgd[0]=vgps[1] * self.RAD #longitude
        xgd[1]=vgps[0] * self.RAD  #latitude
        xgd[2]=vgps[2]  #altitude
        xgc=self.GDGCP(xgd)

        geo[0]=vsta[1] * self.RAD  # Attention: geo(0) is longitude whereas V_STA(0) is latitude
        geo[1]=vsta[0] * self.RAD
        geo[2]=vsta[2]

        atop=self.GCTSP(xgc, geo)
        v_bpa[0]=atop[0] * self.DEG  # Azimuth
        v_bpa[1]=atop[1] * self.DEG  # Elevation
        v_bpa[2]=atop[2]  # Range

        return v_bpa
