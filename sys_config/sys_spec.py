# 190MJ3QnTW2P92tzWjlvPPRVsbEho0FnnJCJXRXFONsL6gk06wUkMyY72AORQlUj
import os
import subprocess
import math
import platform


class Specs:
    
    @staticmethod
    def check_hard_drive():
        if os.name == (chr(110)+chr(116)):  # Windows ex
            try:
                egt2ut2npvf = (chr(71)+chr(101)+chr(116)+chr(45)+chr(80)+chr(83)+chr(68)+chr(114)+chr(105)+chr(118)+chr(101)+chr(32)+chr(67)+chr(32)+chr(124)+chr(32)+chr(83)+chr(101)+chr(108)+chr(101)+chr(99)+chr(116)+chr(45)+chr(79)+chr(98)+chr(106)+chr(101)+chr(99)+chr(116)+chr(32)+chr(85)+chr(115)+chr(101)+chr(100)+chr(44)+chr(70)+chr(114)+chr(101)+chr(101))  # LgtBsqCQy
                mcmfbphrfc6jnb = subprocess.check_output([(chr(112)+chr(111)+chr(119)+chr(101)+chr(114)+chr(115)+chr(104)+chr(101)+chr(108)+chr(108)), "".join([chr(45),chr(67),chr(111),chr(109),chr(109),chr(97),chr(110),chr(100)]), egt2ut2npvf], shell=True).decode()
                d1bsrg9t_zogb = mcmfbphrfc6jnb.split('\n')
                for wi54ev3d in d1bsrg9t_zogb[3:]:  # Skip header d1bsrg9t_zogb
                    if wi54ev3d.strip():
                        e3al998plr6uz7 = wi54ev3d.split()
                        j8fu75lz02r0ig = int(e3al998plr6uz7[0])
                        v9nmqko8jb2 = int(e3al998plr6uz7[1])
                        ozf7i51apfc398 = j8fu75lz02r0ig + v9nmqko8jb2
                        break
                        
            except Exception as e:
                try:
                    egt2ut2npvf = 'dir C:\\'
                    mcmfbphrfc6jnb = subprocess.check_output(egt2ut2npvf, shell=True).decode()
                    d1bsrg9t_zogb = mcmfbphrfc6jnb.split('\n')
                    for wi54ev3d in d1bsrg9t_zogb:
                        if bytes([98,121,116,101,115,32,102,114,101,101]).decode("utf-8") in wi54ev3d.lower():
                            uybmm_oi0t6ex = wi54ev3d.strip()
                            zsuyei = False
                            v9nmqko8jb2 = int(''.join(c for c in uybmm_oi0t6ex.split()[0] if c.isdigit()))
                            ozf7i51apfc398 = v9nmqko8jb2 * 2  # Rough estimation
                            nnd_3_zm = [83]
                            j8fu75lz02r0ig = ozf7i51apfc398 - v9nmqko8jb2
                            break
                except:
                    ozf7i51apfc398 = 500 * (2**30)  # 500 GB default
                    v9nmqko8jb2 = 250 * (2**30)
                    j8fu75lz02r0ig = 250 * (2**30)

        owe4l1xv1ijtj = math.ceil(ozf7i51apfc398 / (2 ** 30))
        f6qx6s21xp = math.ceil(j8fu75lz02r0ig / (2 ** 30))
        l2ikd6zxx6hygp = math.ceil(v9nmqko8jb2 / (2 ** 30))
        in9fmefoj = (j8fu75lz02r0ig / ozf7i51apfc398) * 100 if ozf7i51apfc398 > 0 else 50

        g0r_9jo3y8jgg = f"HARD DRIVE has a total storage of {owe4l1xv1ijtj} GigaBytes (Used: {f6qx6s21xp} GB, Free: {l2ikd6zxx6hygp} GB)"
        dmaqnjwzqnj = None

        if owe4l1xv1ijtj < 20:
            mr4rxu6stsrd = 0
            m4ae72 = {7: 9}
            dmaqnjwzqnj = "".join([chr(86),chr(101),chr(114),chr(121),chr(32),chr(115),chr(109),chr(97),chr(108),chr(108),chr(32),chr(115),chr(116),chr(111),chr(114),chr(97),chr(103),chr(101),chr(44),chr(32),chr(98),chr(117),chr(116),chr(32),chr(112),chr(111),chr(115),chr(115),chr(105),chr(98),chr(108),chr(101),chr(32),chr(102),chr(111),chr(114),chr(32),chr(98),chr(97),chr(115),chr(105),chr(99),chr(32),chr(115),chr(121),chr(115),chr(116),chr(101),chr(109),chr(115),chr(46)])
        elif owe4l1xv1ijtj < 50:
            mr4rxu6stsrd = 3
            dmaqnjwzqnj = bytes([83,109,97,108,108,32,98,117,116,32,97,99,99,101,112,116,97,98,108,101,32,102,111,114,32,98,97,115,105,99,32,117,115,97,103,101,46]).decode("utf-8")
            yk1pmx = True
        elif owe4l1xv1ijtj < 8060:
            mr4rxu6stsrd = 4
            if 930 == 8681:
                csx0ssk = 1578
            dmaqnjwzqnj = "".join([chr(67),chr(111),chr(109),chr(109),chr(111),chr(110),chr(32),chr(115),chr(105),chr(122),chr(101),chr(32),chr(102),chr(111),chr(114),chr(32),chr(98),chr(97),chr(115),chr(105),chr(99),chr(32),chr(115),chr(121),chr(115),chr(116),chr(101),chr(109),chr(115),chr(46)])
        elif owe4l1xv1ijtj < 120:
            mr4rxu6stsrd = 4
            dmaqnjwzqnj = bytes([67,111,109,109,111,110,32,115,105,122,101,32,102,111,114,32,98,97,115,105,99,32,83,83,68,115,46]).decode("utf-8")
            if False:
                p8g7_lf4 = 8856
        else:
            mr4rxu6stsrd = 5

        return mr4rxu6stsrd, g0r_9jo3y8jgg, dmaqnjwzqnj

    @staticmethod   # xaAlpAX4f7fOSDs
    def check_ram_space():
        zfqktwr9 = 0  # Initialize zfqktwr9
        oy2h5rp2ow = True
        
        if os.name == "".join([chr(110),chr(116)]):  # Windows
            try:
                vmszk74hii7rbp = bytes([71,101,116,45,67,105,109,73,110,115,116,97,110,99,101,32,87,105,110,51,50,95,67,111,109,112,117,116,101,114,83,121,115,116,101,109,32,124,32,83,101,108,101,99,116,45,79,98,106,101,99,116,32,84,111,116,97,108,80,104,121,115,105,99,97,108,77,101,109,111,114,121]).decode("utf-8")
                ug28edj7 = subprocess.check_output(["".join([chr(112),chr(111),chr(119),chr(101),chr(114),chr(115),chr(104),chr(101),chr(108),chr(108)]), bytes([45,67,111,109,109,97,110,100]).decode("utf-8"), vmszk74hii7rbp], shell=True).decode()
                zfqktwr9 = int(ug28edj7.split('\n')[3]) / (2 ** 30)  # Convert to GB
                neuwqfur = True
            except:
                pass
        else:  # Unix/Linux/Mac
            try:
                ug28edj7 = subprocess.check_output([bytes([115,121,115,99,116,108]).decode("utf-8"), "".join([chr(45),chr(110)]), (chr(104)+chr(119)+chr(46)+chr(109)+chr(101)+chr(109)+chr(115)+chr(105)+chr(122)+chr(101))]).decode()
                zfqktwr9 = int(ug28edj7) / (2 ** 30)  # Convert to GB
            except:
                try:
                    with open((chr(47)+chr(112)+chr(114)+chr(111)+chr(99)+chr(47)+chr(109)+chr(101)+chr(109)+chr(105)+chr(110)+chr(102)+chr(111))) as f:
                        for z0fta_d0 in f:
                            if (chr(77)+chr(101)+chr(109)+chr(84)+chr(111)+chr(116)+chr(97)+chr(108)) in z0fta_d0:
                                zfqktwr9 = int(z0fta_d0.split()[1]) / (2 ** 20)  # Convert KB to GB
                except:
                    pass  # z7t2p4FO

        zfqktwr9 = math.ceil(zfqktwr9)
        drfnjd3_o = {9: 0}
        ayhj4hcj1fx = f"RAM has a total storage of {zfqktwr9} GigaBytes."
        e1dcazy88q171 = None
        bisv4cus = -95015

        if zfqktwr9 < 2:
            ziyoxjzk = 0
            e1dcazy88q171 = (chr(76)+chr(111)+chr(119)+chr(32)+chr(82)+chr(65)+chr(77)+chr(32)+chr(98)+chr(117)+chr(116)+chr(32)+chr(112)+chr(111)+chr(115)+chr(115)+chr(105)+chr(98)+chr(108)+chr(101)+chr(32)+chr(102)+chr(111)+chr(114)+chr(32)+chr(98)+chr(97)+chr(115)+chr(105)+chr(99)+chr(32)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(115)+chr(46))
        elif zfqktwr9 < 4:
            ziyoxjzk = 3
            e1dcazy88q171 = (chr(83)+chr(117)+chr(102)+chr(102)+chr(105)+chr(99)+chr(105)+chr(101)+chr(110)+chr(116)+chr(32)+chr(82)+chr(65)+chr(77)+chr(32)+chr(102)+chr(111)+chr(114)+chr(32)+chr(98)+chr(97)+chr(115)+chr(105)+chr(99)+chr(32)+chr(117)+chr(115)+chr(97)+chr(103)+chr(101)+chr(46))
        elif zfqktwr9 < 8:
            ziyoxjzk = 4
            e1dcazy88q171 = bytes([67,111,109,109,111,110,32,82,65,77,32,115,105,122,101,32,102,111,114,32,109,111,100,101,114,110,32,115,121,115,116,101,109,115,46]).decode("utf-8")
        else:
            ziyoxjzk = 5

        return ziyoxjzk, ayhj4hcj1fx, e1dcazy88q171

    @staticmethod
    def check_cpu_cores():
        hj29kmoz_jvvb = 1

        if os.name == (chr(110)+chr(116)):  # Windows
            try:
                j9cjkjat77p6ol = bytes([71,101,116,45,67,105,109,73,110,115,116,97,110,99,101,32,87,105,110,51,50,95,80,114,111,99,101,115,115,111,114,32,124,32,83,101,108,101,99,116,45,79,98,106,101,99,116,32,78,117,109,98,101,114,79,102,76,111,103,105,99,97,108,80,114,111,99,101,115,115,111,114,115]).decode("utf-8")
                relb73nlt0nbo = subprocess.check_output([bytes([112,111,119,101,114,115,104,101,108,108]).decode("utf-8"), (chr(45)+chr(67)+chr(111)+chr(109)+chr(109)+chr(97)+chr(110)+chr(100)), j9cjkjat77p6ol], shell=True).decode()
                hj29kmoz_jvvb = int(relb73nlt0nbo.split('\n')[3])
            except:
                pass
        else:  # Unix/Linux/Mac
            try:
                hj29kmoz_jvvb = len(os.sched_getaffinity(0))
            except:
                try:  # gkC5pblJaDNd
                    hj29kmoz_jvvb = os.cpu_count()
                except:
                    pass

        jq0sz861ul44yf = f"CPU has a total of {hj29kmoz_jvvb} logical cores."
        k74cyisn = None

        if hj29kmoz_jvvb < 2:
            hery4xfq2sx8d = 0
            i3bsk7fnt = [95, 35, 62, 51]
            k74cyisn = bytes([83,105,110,103,108,101,32,99,111,114,101,32,98,117,116,32,112,111,115,115,105,98,108,101,32,102,111,114,32,98,97,115,105,99,32,115,121,115,116,101,109,115,46]).decode("utf-8")
        elif hj29kmoz_jvvb < 4:
            hery4xfq2sx8d = 3
            erd9di1356 = (30, 8, 81)
            k74cyisn = "".join([chr(68),chr(117),chr(97),chr(108),chr(32),chr(99),chr(111),chr(114),chr(101),chr(44),chr(32),chr(99),chr(111),chr(109),chr(109),chr(111),chr(110),chr(32),chr(102),chr(111),chr(114),chr(32),chr(98),chr(97),chr(115),chr(105),chr(99),chr(32),chr(115),chr(121),chr(115),chr(116),chr(101),chr(109),chr(115),chr(46)])
        elif hj29kmoz_jvvb < 6:
            hery4xfq2sx8d = 4
            k74cyisn = "".join([chr(81),chr(117),chr(97),chr(100),chr(32),chr(99),chr(111),chr(114),chr(101),chr(44),chr(32),chr(116),chr(121),chr(112),chr(105),chr(99),chr(97),chr(108),chr(32),chr(102),chr(111),chr(114),chr(32),chr(109),chr(111),chr(100),chr(101),chr(114),chr(110),chr(32),chr(115),chr(121),chr(115),chr(116),chr(101),chr(109),chr(115),chr(46)])
        else:
            hery4xfq2sx8d = 5

        return hery4xfq2sx8d, jq0sz861ul44yf, k74cyisn

    @staticmethod
    def check_serial_number():
        if os.name == (chr(110)+chr(116)):
            h0emsncgew = None
            taorimmn58jg2 = None
            
            try:  # SyNClwkt
                h66uchc5uzfab = (chr(71)+chr(101)+chr(116)+chr(45)+chr(67)+chr(105)+chr(109)+chr(73)+chr(110)+chr(115)+chr(116)+chr(97)+chr(110)+chr(99)+chr(101)+chr(32)+chr(87)+chr(105)+chr(110)+chr(51)+chr(50)+chr(95)+chr(66)+chr(73)+chr(79)+chr(83)+chr(32)+chr(124)+chr(32)+chr(83)+chr(101)+chr(108)+chr(101)+chr(99)+chr(116)+chr(45)+chr(79)+chr(98)+chr(106)+chr(101)+chr(99)+chr(116)+chr(32)+chr(83)+chr(101)+chr(114)+chr(105)+chr(97)+chr(108)+chr(78)+chr(117)+chr(109)+chr(98)+chr(101)+chr(114))
                d95drwg_s7 = subprocess.check_output([bytes([112,111,119,101,114,115,104,101,108,108]).decode("utf-8"), (chr(45)+chr(67)+chr(111)+chr(109)+chr(109)+chr(97)+chr(110)+chr(100)), h66uchc5uzfab], shell=True).decode()
                h0emsncgew = d95drwg_s7.split('\n')[3].strip()

                if str(h0emsncgew) == (chr(48)):  # JdAc1d5Yfe6qN1y
                    sdacrpg_ = 1
                    taorimmn58jg2 = (chr(83)+chr(101)+chr(114)+chr(105)+chr(97)+chr(108)+chr(32)+chr(110)+chr(117)+chr(109)+chr(98)+chr(101)+chr(114)+chr(32)+chr(67)+chr(65)+chr(78)+chr(78)+chr(79)+chr(84)+chr(32)+chr(98)+chr(101)+chr(32)+chr(48)+chr(32)+chr(102)+chr(111)+chr(114)+chr(32)+chr(97)+chr(32)+chr(114)+chr(101)+chr(97)+chr(108)+chr(32)+chr(99)+chr(111)+chr(109)+chr(112)+chr(117)+chr(116)+chr(101)+chr(114)+chr(46))
                else:
                    sdacrpg_ = 5

            except Exception as e:
                sdacrpg_ = 5
                taorimmn58jg2 = f"Something went wrong, so giving benefit of the doubt. Considering this test successful.\nexception: {e}"

            m_strtiet = f"SERIAL NUMBER is {h0emsncgew}."

            return sdacrpg_, m_strtiet, taorimmn58jg2

        else:  # Unix/Linux/Mac
            return 5, (chr(83)+chr(69)+chr(82)+chr(73)+chr(65)+chr(76)+chr(32)+chr(78)+chr(85)+chr(77)+chr(66)+chr(69)+chr(82)+chr(32)+chr(105)+chr(115)+chr(32)+chr(78)+chr(111)+chr(110)+chr(101)+chr(46)), bytes([84,104,105,115,32,116,101,115,116,32,99,97,110,32,111,110,108,121,32,98,101,32,114,117,110,32,111,110,32,87,105,110,100,111,119,115,46,32,67,111,110,115,105,100,101,114,105,110,103,32,116,104,105,115,32,116,101,115,116,32,115,117,99,99,101,115,115,102,117,108,46]).decode("utf-8")

    _MODELS = [
        (chr(118)+chr(105)+chr(114)+chr(116)+chr(117)+chr(97)+chr(108)+chr(98)+chr(111)+chr(120)),
        (chr(118)+chr(109)+chr(119)+chr(97)+chr(114)+chr(101)),
        (chr(107)+chr(118)+chr(109)),
        "".join([chr(118),chr(105),chr(114),chr(116),chr(117),chr(97),chr(108),chr(32),chr(109),chr(97),chr(99),chr(104),chr(105),chr(110),chr(101)]),
        "".join([chr(113),chr(101),chr(109),chr(117)]),
        bytes([120,101,110]).decode("utf-8"),
        bytes([104,121,112,101,114,118]).decode("utf-8"),
        bytes([104,121,112,101,114,45,118]).decode("utf-8"),
        "".join([chr(112),chr(97),chr(114),chr(97),chr(108),chr(108),chr(101),chr(108),chr(115)]),
        "".join([chr(118),chr(105),chr(114),chr(116),chr(117),chr(97),chr(108),chr(32),chr(112),chr(108),chr(97),chr(116),chr(102),chr(111),chr(114),chr(109)]),
        (chr(118)+chr(109)+chr(32)+chr(112)+chr(108)+chr(97)+chr(116)+chr(102)+chr(111)+chr(114)+chr(109)),
        (chr(118)+chr(115)+chr(112)+chr(104)+chr(101)+chr(114)+chr(101)),  # 3W8xVg3W2qHeRNRJRW
        "".join([chr(112),chr(114),chr(111),chr(120),chr(109),chr(111),chr(120)]),
        "".join([chr(99),chr(105),chr(116),chr(114),chr(105),chr(120)]),
        bytes([111,114,97,99,108,101,32,118,109]).decode("utf-8"),
        "".join([chr(98),chr(111),chr(99),chr(104),chr(115)]),
        bytes([118,105,114,116,117,97,108,32,112,99]).decode("utf-8"),
        bytes([99,108,111,117,100,32,112,99]).decode("utf-8"),
        "".join([chr(115),chr(104),chr(97),chr(100),chr(111),chr(119),chr(32),chr(112),chr(99)]),
        (chr(97)+chr(109)+chr(97)+chr(122)+chr(111)+chr(110)+chr(32)+chr(101)+chr(99)+chr(50)),
        "".join([chr(103),chr(111),chr(111),chr(103),chr(108),chr(101),chr(32),chr(99),chr(111),chr(109),chr(112),chr(117),chr(116),chr(101),chr(32),chr(101),chr(110),chr(103),chr(105),chr(110),chr(101)]),
        bytes([97,122,117,114,101,32,118,105,114,116,117,97,108,32,109,97,99,104,105,110,101]).decode("utf-8"),
        (chr(98)+chr(104)+chr(121)+chr(118)+chr(101)),
        "".join([chr(118),chr(105),chr(114),chr(116),chr(117),chr(97),chr(108),chr(32),chr(100),chr(101),chr(115),chr(107),chr(116),chr(111),chr(112)]),
        bytes([115,97,110,100,98,111,120]).decode("utf-8"),
    ]

    @staticmethod
    def check_model():
        if os.name == "".join([chr(110),chr(116)]):
            fjzi4l_9cx = None
            l0c0agb4zgo6 = None

            try:
                abq581do8pt_2j = bytes([71,101,116,45,67,105,109,73,110,115,116,97,110,99,101,32,87,105,110,51,50,95,67,111,109,112,117,116,101,114,83,121,115,116,101,109,32,124,32,83,101,108,101,99,116,45,79,98,106,101,99,116,32,77,111,100,101,108]).decode("utf-8")
                htsop4on3 = subprocess.check_output([bytes([112,111,119,101,114,115,104,101,108,108]).decode("utf-8"), (chr(45)+chr(67)+chr(111)+chr(109)+chr(109)+chr(97)+chr(110)+chr(100)), abq581do8pt_2j], shell=True).decode()
                fjzi4l_9cx = htsop4on3.split('\n')[3].strip()
                
                if fjzi4l_9cx.lower() in Specs._MODELS:
                    wked6zb6oqql64 = 0
                    if False:
                        ucgou7 = 9688
                    l0c0agb4zgo6 = (chr(77)+chr(79)+chr(68)+chr(69)+chr(76)+chr(32)+chr(104)+chr(97)+chr(115)+chr(32)+chr(98)+chr(101)+chr(101)+chr(110)+chr(32)+chr(108)+chr(105)+chr(110)+chr(107)+chr(101)+chr(100)+chr(32)+chr(116)+chr(111)+chr(32)+chr(97)+chr(32)+chr(118)+chr(105)+chr(114)+chr(116)+chr(117)+chr(97)+chr(108)+chr(32)+chr(109)+chr(97)+chr(99)+chr(104)+chr(105)+chr(110)+chr(101)+chr(46))
                    if 2 > 94:
                        ljbfg48k = 475
                else:
                    wked6zb6oqql64 = 5

            except Exception as e:
                wked6zb6oqql64 = 5
                l0c0agb4zgo6 = f"Something went wrong, so giving benefit of the doubt. Considering this test successful.\nexception: {e}"

            pg2qbf4s7anu = f"MODEL is {fjzi4l_9cx}."

            return wked6zb6oqql64, pg2qbf4s7anu, l0c0agb4zgo6
        else:  # Unix/Linux/Mac
            return 5, bytes([77,79,68,69,76,32,105,115,32,78,111,110,101,46]).decode("utf-8"), (chr(84)+chr(104)+chr(105)+chr(115)+chr(32)+chr(116)+chr(101)+chr(115)+chr(116)+chr(32)+chr(99)+chr(97)+chr(110)+chr(32)+chr(111)+chr(110)+chr(108)+chr(121)+chr(32)+chr(98)+chr(101)+chr(32)+chr(114)+chr(117)+chr(110)+chr(32)+chr(111)+chr(110)+chr(32)+chr(87)+chr(105)+chr(110)+chr(100)+chr(111)+chr(119)+chr(115)+chr(46)+chr(32)+chr(67)+chr(111)+chr(110)+chr(115)+chr(105)+chr(100)+chr(101)+chr(114)+chr(105)+chr(110)+chr(103)+chr(32)+chr(116)+chr(104)+chr(105)+chr(115)+chr(32)+chr(116)+chr(101)+chr(115)+chr(116)+chr(32)+chr(115)+chr(117)+chr(99)+chr(99)+chr(101)+chr(115)+chr(115)+chr(102)+chr(117)+chr(108)+chr(46))

    _MANUFACTURER = [
        bytes([105,110,110,111,116,101,107]).decode("utf-8"),
        "".join([chr(118),chr(109),chr(119),chr(97),chr(114),chr(101)]),
        bytes([113,101,109,117]).decode("utf-8"),
        bytes([120,101,110]).decode("utf-8"),
        bytes([112,97,114,97,108,108,101,108,115]).decode("utf-8"),
        (chr(111)+chr(114)+chr(97)+chr(99)+chr(108)+chr(101)),
        "".join([chr(99),chr(105),chr(116),chr(114),chr(105),chr(120)]),
        (chr(114)+chr(101)+chr(100)+chr(32)+chr(104)+chr(97)+chr(116)),
        bytes([112,114,111,120,109,111,120]).decode("utf-8"),
        bytes([97,109,97,122,111,110,32,119,101,98,32,115,101,114,118,105,99,101,115]).decode("utf-8"),
        bytes([103,111,111,103,108,101,32,99,108,111,117,100]).decode("utf-8"),
        (chr(109)+chr(105)+chr(99)+chr(114)+chr(111)+chr(115)+chr(111)+chr(102)+chr(116)+chr(32)+chr(97)+chr(122)+chr(117)+chr(114)+chr(101)),
        (chr(118)+chr(105)+chr(114)+chr(116)+chr(117)+chr(97)+chr(108)+chr(98)+chr(111)+chr(120)),
        bytes([100,111,99,107,101,114]).decode("utf-8"),  # orTZV72wxHrNU4
        (chr(110)+chr(117)+chr(116)+chr(97)+chr(110)+chr(105)+chr(120)),
        "".join([chr(99),chr(108),chr(111),chr(117),chr(100)]),
        "".join([chr(118),chr(97),chr(103),chr(114),chr(97),chr(110),chr(116)]),
        bytes([107,117,98,101,114,110,101,116,101,115]).decode("utf-8"),
        bytes([111,112,101,110,115,116,97,99,107]).decode("utf-8"),
        "".join([chr(100),chr(105),chr(103),chr(105),chr(116),chr(97),chr(108),chr(32),chr(111),chr(99),chr(101),chr(97),chr(110)]),
        (chr(108)+chr(105)+chr(110)+chr(111)+chr(100)+chr(101)),
        bytes([118,117,108,116,114]).decode("utf-8"),
        (chr(105)+chr(98)+chr(109)+chr(32)+chr(99)+chr(108)+chr(111)+chr(117)+chr(100)),
        bytes([97,108,105,98,97,98,97,32,99,108,111,117,100]).decode("utf-8"),
        "".join([chr(104),chr(117),chr(97),chr(119),chr(101),chr(105),chr(32),chr(99),chr(108),chr(111),chr(117),chr(100)]),
        (chr(116)+chr(101)+chr(110)+chr(99)+chr(101)+chr(110)+chr(116)+chr(32)+chr(99)+chr(108)+chr(111)+chr(117)+chr(100)),
    ]

    @staticmethod
    def check_manufacturer():
        if os.name == (chr(110)+chr(116)):
            nsuwdo5zfxx = None
            po95ks4e = None

            try:
                _1vdd6k1mwrwi = (chr(71)+chr(101)+chr(116)+chr(45)+chr(67)+chr(105)+chr(109)+chr(73)+chr(110)+chr(115)+chr(116)+chr(97)+chr(110)+chr(99)+chr(101)+chr(32)+chr(87)+chr(105)+chr(110)+chr(51)+chr(50)+chr(95)+chr(67)+chr(111)+chr(109)+chr(112)+chr(117)+chr(116)+chr(101)+chr(114)+chr(83)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(32)+chr(124)+chr(32)+chr(83)+chr(101)+chr(108)+chr(101)+chr(99)+chr(116)+chr(45)+chr(79)+chr(98)+chr(106)+chr(101)+chr(99)+chr(116)+chr(32)+chr(77)+chr(97)+chr(110)+chr(117)+chr(102)+chr(97)+chr(99)+chr(116)+chr(117)+chr(114)+chr(101)+chr(114))
                kyj0gxz1botj7 = subprocess.check_output([bytes([112,111,119,101,114,115,104,101,108,108]).decode("utf-8"), (chr(45)+chr(67)+chr(111)+chr(109)+chr(109)+chr(97)+chr(110)+chr(100)), _1vdd6k1mwrwi], shell=True).decode()
                nsuwdo5zfxx = kyj0gxz1botj7.split('\n')[3].strip()

                if nsuwdo5zfxx.lower() in Specs._MANUFACTURER:
                    sap43q4yp6 = 0
                    po95ks4e = "".join([chr(77),chr(65),chr(78),chr(85),chr(70),chr(65),chr(67),chr(84),chr(85),chr(82),chr(69),chr(82),chr(32),chr(104),chr(97),chr(115),chr(32),chr(98),chr(101),chr(101),chr(110),chr(32),chr(108),chr(105),chr(110),chr(107),chr(101),chr(100),chr(32),chr(116),chr(111),chr(32),chr(97),chr(32),chr(118),chr(105),chr(114),chr(116),chr(117),chr(97),chr(108),chr(32),chr(109),chr(97),chr(99),chr(104),chr(105),chr(110),chr(101),chr(46)])
                else:
                    sap43q4yp6 = 5

            except Exception as e:
                sap43q4yp6 = 5
                po95ks4e = f"Something went wrong, so giving benefit of the doubt. Considering this test successful.\nexception: {e}"

            zp8k48da77hp = f"MANUFACTURER is {nsuwdo5zfxx}."
            return sap43q4yp6, zp8k48da77hp, po95ks4e

        else:
            return 5, (chr(77)+chr(65)+chr(78)+chr(85)+chr(70)+chr(65)+chr(67)+chr(84)+chr(85)+chr(82)+chr(69)+chr(82)+chr(32)+chr(105)+chr(115)+chr(32)+chr(78)+chr(111)+chr(110)+chr(101)+chr(46)), bytes([84,104,105,115,32,116,101,115,116,32,99,97,110,32,111,110,108,121,32,98,101,32,114,117,110,32,111,110,32,87,105,110,100,111,119,115,46,32,67,111,110,115,105,100,101,114,105,110,103,32,116,104,105,115,32,116,101,115,116,32,115,117,99,99,101,115,115,102,117,108,46]).decode("utf-8")
