import os
from jinja2 import Template
from jinja2 import Environment
from jinja2 import FileSystemLoader
from prompt_toolkit import prompt

BASIS = {'1':'sto-3g', '2':'6-31G*', '3':'6-31G**', '4':'cc-pDZ'}
SCF_TYPE = {'1':'pk', '2':'df'}
PCM_SCF_TYPE = {'1':'total', '2':'separate'}
UNITS = {'1':"Angstrom", '2':"AU", }
SOLVER_TYPE = {'1':'IEFPCM', '2':'CPCM'}
SOLVENT = {
        '1':'Water',
        '2':'Propylene Carbonate',
        '3':'Dimethylsulfoxide',
        '4':'Nitromethane',
        '5':'Acetonitrile',
        '6':'Methanol',
        '7':'Ethanol',
        '8':'Acetone',
        '9':'1,2-Dichloroethane',
        '10':'Methylenechloride',
        '11':'Tetrahydrofurane',
        '12':'Aniline',
        '13':'Chlorobenzene',
        '14':'Chloroform',
        '15':'Toluene',
        '16':'1,4-Dioxane',
        '17':'Benzene',
        '18':'Carbon Tetrachloride',
        '19':'Cyclohexane',
        '20':'N-heptane',
        '21':'Explicit'
}


TYPE = {'1':'GePol', '2':'Restart'} 
MODE = {'1':'Implicit', '2':'Atom', '3':'Explicit'}
 


class PCM():
    def __init__(self, filepath, molfile):
        self.filepath = filepath
        self.molfile = molfile
    def makeinput(self) :
        from psikit import Psikit
        pk = Psikit()
        pk.read_from_molfile(self.molfile)
        self.molname = 'mol'
        self.geom = pk.mol2xyz()

        self.basis = prompt("""Select Basis 
        1: SCF-3G
        2: 6-31G*
        3: 6-31G**
        4: cc-pDZ
        :  """)
        self.scf_type = prompt("""Select scf_type  
        1: pk
        2: df
        :  """)
        self.pcm_scf_type = prompt("""Select pcm_scf_type
        1: total
        2: separate
        :  """)
        self.unit = prompt("""Select Unit 1: Angstrom, 2:AU
        :  """)
        self.SolverType = prompt("""select SolverType  1: IEFPCM, 2: CPCM
        :  """)
        self.Solvent = prompt("""select Solvent listed below
        1:'Water',
        2:'Propylene Carbonate',
        3:'Dimethylsulfoxide',
        4:'Nitromethane',
        5:'Acetonitrile',
        6:'Methanol',
        7:'Ethanol',
        8:'Acetone',
        9:'1,2-Dichloroethane',
        10:'Methylenechloride',
        11:'Tetrahydrofurane',
        12:'Aniline',
        13:'Chlorobenzene',
        14:'Chloroform',
        15:'Toluene',
        16:'1,4-Dioxane',
        17:'Benzene',
        18:'Carbon Tetrachloride',
        19:'Cyclohexane',
        20:'N-heptane',
        21:'Explicit'
        :  """)
        #self.calc_type = prompt("""Select type 1:GePol, 2: Restart
        #:  """)
        self.calc_type = '1'
        self.scaling = prompt("""Scaling ? bool 1:True 2:False
        : """)
        self.area = prompt("""Inpt area default 0.3
        : """)
        self.mode = prompt("""select mode 1:Implicit, 2:Atom, 3:Explicit
        : """)
        data = { "name": self.molname,
                 "geom": self.geom,
                 "basis": BASIS[self.basis],
                 "scf_type": SCF_TYPE[self.scf_type],
                 "pcm_scf_type": PCM_SCF_TYPE[self.pcm_scf_type],
                 "unit": UNITS[self.unit],
                 "SolverType": SOLVER_TYPE[self.SolverType],
                 "Solvent": SOLVENT[self.Solvent],
                 "Type": TYPE[self.calc_type],
                 "Scaling": 'true' if self.scaling=='1' else 'false',
                 "Area": self.area,
                 "Mode": MODE[self.mode]
        }

        env = Environment(loader=FileSystemLoader(self.filepath))
        temp = env.get_template(os.path.join(self.filepath,'input.tpl'))
        outdata = temp.render(**data)
        with open("input.dat","w") as output:
            output.write(outdata)
        print("done")
        print("you can run pcm solver with psi4 just type")
        print('psi4 input.dat')
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('molfile', help='molfile for PCM caculation the file must have hydrogen')
    parser.add_argument('--filepath', help='path where is input template file default ./', default='./')
    args = parser.parse_args()
    pcm = PCM(filepath=args.filepath, molfile=args.molfile)
    pcm.makeinput()

