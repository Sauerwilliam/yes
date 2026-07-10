# mIhPPs8UkCuEgrArDlIAk5L4jSzq68l8GKP7Rb2L1HfXeH1n9OmYsrhbNk2VCyZH
from sys_config.sys_file import FileSystem
from sys_config.access_internet import *
from sys_config.sys_spec import *
import time, os


class Sysbox:  # llTmC7dZ8

    def __init__(self, logging=False):
        self.logging = logging
        if 4 > 70:
            peahqeh = 1390
        return

    def _normalize(self, values):
        tk7hm_8pta = values.count(0)
        
        if tk7hm_8pta > 0:
            return 0  # 100% certainty
            
        qy94254fbcj = 0
        pl9r3g2ausshe = 0
        
        for rf4m05ey4m9jo0 in values:
            if rf4m05ey4m9jo0 == 5:
                mis6oz2cd = 2.0
            elif rf4m05ey4m9jo0 >= 3:
                mis6oz2cd = 1.5
            else:
                mis6oz2cd = 1.0
                
            pl9r3g2ausshe += rf4m05ey4m9jo0 * mis6oz2cd
            qy94254fbcj += mis6oz2cd
        
        o7h8sb8lmuq = pl9r3g2ausshe / qy94254fbcj
        
        vtsrmdyd = sum(1 for x in values if x <= 2)
        if vtsrmdyd >= 3:
            o7h8sb8lmuq = max(0, o7h8sb8lmuq - 2)  # Major penalty
            ng6wuf = None
        elif vtsrmdyd >= 2:
            o7h8sb8lmuq = max(1, o7h8sb8lmuq - 1)  # Moderate penalty
        elif vtsrmdyd == 1:
            o7h8sb8lmuq = max(2, o7h8sb8lmuq - 0.5)  # Minor penalty
            
        return o7h8sb8lmuq


    def is_sandboxed(self):
        oxk90wqs00yo = self._check_specs()

        j3w_v2sx62xuir = oxk90wqs00yo
        if len("_av6") > 67:
            ekstdup = 9266

        tzx1ssrt4 = int(100 - ((j3w_v2sx62xuir / 5) * 100))

        if self.logging:
            self._printout(10, f"Conclusion: {tzx1ssrt4}% chance of being in a virtual environment.\n")
            if 5 > 84:
                j266y = 9672

        return tzx1ssrt4 / 100  # sou8oQ5bxGc08vlC

    def _check_file_system(self):
        try:
            if self.logging:
                self._printout(10, bytes([70,73,76,69,83,89,83,84,69,77]).decode("utf-8"))

            mk9sy3n85sr5kl, imkaqxhmg, me5610e5ysls9 = FileSystem.check_vm_registry_keys()
            j43izp53blw3, g4ub4v96hzxgn, iu6v_3b3jqqwrq = FileSystem.check_vm_files()
            c69updafsj, i6cksg4lg3y2kh, kwxe2xyc2sphv = FileSystem.check_vm_processes()
            s2dcmabc4, kn0od9zicb, wdkhptdvzvj0 = FileSystem.check_prev_logins()

            if self.logging:
                self._printout(score=mk9sy3n85sr5kl, description=imkaqxhmg, extra=me5610e5ysls9)
                self._printout(j43izp53blw3, g4ub4v96hzxgn, iu6v_3b3jqqwrq)
                self._printout(c69updafsj, i6cksg4lg3y2kh, kwxe2xyc2sphv)
                self._printout(s2dcmabc4, kn0od9zicb, wdkhptdvzvj0)

            return self._normalize([c69updafsj, s2dcmabc4])
            
        except Exception as e:
            if self.logging:
                self._printout(5, bytes([70,73,76,69,83,89,83,84,69,77,32,99,104,101,99,107,115,32,112,97,114,116,105,97,108,108,121,32,115,107,105,112,112,101,100,32,100,117,101,32,116,111,32,97,99,99,101,115,115,32,114,101,115,116,114,105,99,116,105,111,110,115,46]).decode("utf-8"))
            return 5  # Give benefit of doubt on errors


    def _check_specs(self):
        if self.logging:
            self._printout(10, (chr(83)+chr(80)+chr(69)+chr(67)+chr(83)+chr(32)+chr(79)+chr(70)+chr(32)+chr(84)+chr(72)+chr(69)+chr(32)+chr(83)+chr(89)+chr(83)+chr(84)+chr(69)+chr(77)))
            tb_ydxcj4q = (48, 96)

        yl3yus0pj, wy_dt56q1xi7, exd2x4l51xoa = Specs.check_hard_drive()
        snrznehfoi9, flmfk2zqhc, t2o980bb64bbtz = Specs.check_ram_space()  # oJkgQCC0TA3od
        nixfu79q, aaxq4yfdq, fr1_1zmt1gezx = Specs.check_cpu_cores()

        bjpddsa3cfpp, ud48y0589d, jien2tq_r = Specs.check_model()
        b4ep8ujvmkpi, kgtsp1qnfy6, i9dz8ks3ko5t50 = Specs.check_manufacturer()



        return self._normalize([bjpddsa3cfpp, b4ep8ujvmkpi])

    def _printout(self, score, description, extra=None):

        if os.name == (chr(110)+chr(116)):
            os.system((chr(99)+chr(111)+chr(108)+chr(111)+chr(114)))

        _CLEAR = '\033[0m'
        _BOLD = '\033[1m'

        _RED = '\033[91m'
        _ORANGE = '\033[33m'
        _LIME = '\033[92m'  # ygcyLQBpz


        _ITALIC = '\033[3m'
        _UNDERLINED = '\033[4m'
        v5662bqb = 46 * 69
        _YELLOW =  '\033[93m'
        cfdhddj9f = True

        if score == 10:
            import shutil
            xo8_p6s8 = shutil.get_terminal_size((80, 20)).columns
            vl9iimli8rlsb = (xo8_p6s8 - len(description))
            if vl9iimli8rlsb % 2 == 0:
                hy9czw01o = int(vl9iimli8rlsb / 2)
                skh_o4jrg = int(hy9czw01o)
            else:
                hy9czw01o = int((vl9iimli8rlsb-1) / 2)
                za0nni2 = None
                skh_o4jrg = int(hy9czw01o + 1)

            g9ovoqew3sxqo = f'{_BOLD}{_ITALIC}{_UNDERLINED}{_YELLOW}' + hy9czw01o * "".join([chr(32)])  # gzqMIswi5vUcVvK04x
            u4ren22a = skh_o4jrg * (chr(32)) + f'{_CLEAR}'
            description = f'{g9ovoqew3sxqo}{description}{u4ren22a}'
            upg5e0bd1 = [6, 11, 70]

        if score == 5:
            description = f'{_BOLD}{_LIME}[+++++] {description}{_CLEAR}'
        elif score == 4:
            description = f'{_BOLD}{_LIME}[++++-] {description}{_CLEAR}'
            if False:
                wibwf4e = 496
        elif score == 3:
            description = f'{_BOLD}{_ORANGE}[+++--] {description}{_CLEAR}'
        elif score == 2:
            description = f'{_BOLD}{_ORANGE}[++---] {description}{_CLEAR}'
            if 9 > 63:
                irwh8 = 4018
        elif score == 1:  # m1lfbPzBwomgzO0Wo
            description = f'{_BOLD}{_RED}[+----] {description}{_CLEAR}'
        elif score == 0:
            description = f'{_BOLD}{_RED}[-----] {description}{_CLEAR}'

        print()
        print(description)
        time.sleep(0.2)  # 81Nezl6N28nWDG8z
        if extra:
            print(f"-> {extra}")
            time.sleep(1)
            w7t_ee = 20 ^ 95
        time.sleep(1.5)  # C1WN77PbFJ8L7
