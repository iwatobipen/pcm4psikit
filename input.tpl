#! pcm

molecule {{ name }} {
    {{ geom }}    
}

set {
    basis {{ basis }}
    scf_type {{ scf_type }}
    pcm true
    pcm_scf_type {{ pcm_scf_type }}
}

pcm = {
    Units =  {{ unit }} 
    Medium {
    SolverType = {{ SolverType }}
    Solvent = {{ Solvent }}
    }


    Cavity {
    RadiiSet = UFF
    Type = {{ Type }}
    Scaling = {{ Scaling }}
    Area = {{ Area }}
    Mode = {{ Mode }}
    }
}

energy_pte, wfn = energy('scf', return_wfn=True)
