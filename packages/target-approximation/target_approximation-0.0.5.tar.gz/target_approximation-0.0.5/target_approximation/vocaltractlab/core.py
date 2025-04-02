


import numpy as np
import pandas as pd

from typing import List, Optional, Dict, Any, Union, Tuple, Iterable

from target_approximation.vocaltractlab.utils import supraglottal_tiers as vtl_sg_tiers
from target_approximation.vocaltractlab.utils import glottal_tiers as vtl_g_tiers
from target_approximation.vocaltractlab.utils import ms_file_extensions
from target_approximation.vocaltractlab.utils import _tract_params_from_vtl_tractseq
from target_approximation.vocaltractlab.utils import _glottis_params_from_vtl_tractseq
from target_approximation.vocaltractlab.utils import st_to_hz, hz_to_st

from target_approximation.core import TargetSequence
from target_approximation.core import TargetSeries
from target_approximation.tensortract import MotorSequence as TT_MSQ
from target_approximation.tensortract import MotorSeries as TT_MSRS



class SupraGlottalSequence( TargetSequence ):
    def __init__(
            self,
            targets: np.ndarray,
            sg_set: str = 'default',
            ):
        tiers = vtl_sg_tiers[ sg_set ]
        super(SupraGlottalSequence, self).__init__(
            targets=targets,
            tiers=tiers,
            )
        return
    
class GlottalSequence( TargetSequence ):
    def __init__(
            self,
            targets: np.ndarray,
            g_set: str = 'default',
            ):
        tiers = vtl_g_tiers[ g_set ]
        super(GlottalSequence, self).__init__(
            targets=targets,
            tiers=tiers,
            )
        return
    
class MotorSequence( TargetSequence ):
    def __init__(
            self,
            targets: np.ndarray,
            sg_set: str = 'default',
            g_set: str = 'default',
            ):
        tiers = vtl_sg_tiers[ sg_set ] + vtl_g_tiers[ g_set ]
        super(MotorSequence, self).__init__(
            targets=targets,
            tiers=tiers,
            )
        return
    
    def to_series(
            self,
            sr: Optional[ float ] = None,
            ):
        x = MotorSeries.from_sequence( self, sr )
        return x

class SupraGlottalSeries( TargetSeries ):
    def __init__(
            self,
            series: np.ndarray,
            sr: float = None,
            sg_set = 'default',
            ):
        tiers = vtl_sg_tiers[ sg_set ]
        super(SupraGlottalSeries, self).__init__(
            series,
            sr,
            tiers,
            )
        return
    
class GlottalSeries( TargetSeries ):
    def __init__(
            self,
            series: np.ndarray,
            sr: float = None,
            g_set = 'default',
            ):
        tiers = vtl_g_tiers[ g_set ]
        super(GlottalSeries, self).__init__(
            series,
            sr,
            tiers,
            )
        return
    
    def pitch_shift(
            self,
            x: float,
        ):
        # pitch shift is in semitones
        f0_st = hz_to_st(self.series[ 'F0' ])
        f0_shifted = f0_st + x
        self.series[ 'F0' ] = st_to_hz( f0_shifted )
        return
    
class MotorSeries( TargetSeries ):
    def __init__(
            self,
            series: np.ndarray,
            sr: float = None,
            sg_set = 'default',
            g_set = 'default',
            ):
        tiers = vtl_sg_tiers[ sg_set ] + vtl_g_tiers[ g_set ]
        super(MotorSeries, self).__init__(
            series,
            sr,
            tiers,
            )
        self.sg_set = sg_set
        self.g_set = g_set
        return
    
    @classmethod
    def load(
            cls,
            file_path: str,
            sr = None,
            ):
        try:
            return super().load( file_path, sr=sr )
        except ValueError:   
            if file_path.endswith( '.xx' ):
                #series = np.load( file_path )
                pass
            elif any( [
                    file_path.endswith( ext )
                    for ext in ms_file_extensions
                    ] ):
                ms = MotorSequence.load( file_path )
                mss = ms.to_series( sr = sr )
            elif file_path.endswith( '.csv' ):
                mss = pd.read_csv( file_path )
            elif file_path.endswith( '.tsq' ):
                mss = cls.from_vtl_tractseq(
                    file_path,
                    sr = sr,
                    )
            else:
                raise ValueError(
                    f'Unsupported file extension: {file_path}'
                    )
        return cls( mss, sr = sr )
    
    @classmethod
    def from_vtl_tractseq(
            cls,
            path: str,
            sr = None,
            ):
        if sr is None:
            sr = 44100/110
        df_vtp = pd.read_csv(
            path,
            #delim_whitespace = True,#deprecated
            sep='\s+',
            skiprows= lambda x: _tract_params_from_vtl_tractseq(x),
            header = None,
            )
        df_glp = pd.read_csv(
            path,
            #delim_whitespace = True,
            sep='\s+',
            skiprows= lambda x: _glottis_params_from_vtl_tractseq(x),
            header = None,
            )
        x = np.concatenate( [
            df_vtp.to_numpy(),
            df_glp.to_numpy(),
            ],
            axis = 1,
            )
        return cls( x, sr = sr )
    
    def tract( self ):
        x = self.series[ vtl_sg_tiers[ self.sg_set ] ]

        sgs = SupraGlottalSeries(
            series = x,
            sr = self.sr,
            sg_set = self.sg_set,
            )
        
        return sgs
    
    def glottis( self ):
        x = self.series[ vtl_g_tiers[ self.g_set ] ]

        gs = GlottalSeries(
            series = x,
            sr = self.sr,
            g_set = self.g_set,
            )
        
        return gs
    
    def save(
            self,
            file_path: str,
            as_type = 'vtl',
            **kwargs,
            ):
        if as_type in [ 'tt', 'tensortract' ]:
            tt_ms = self.to_tt( **kwargs )
            tt_ms.save( file_path )
        elif as_type in [ 'vtl', 'vocaltractlab' ]:
            super().save( file_path )
        else:
            raise ValueError(
                f'Unsupported arg as_type: {as_type}'
                )
        return
    
    def to_tt(
            self,
            target_sr = 50,
            ):
        x = TT_MSRS( self )
        x.resample( target_sr )
        return x
    
    def pitch_shift(
            self,
            x: float,
        ):
        # pitch shift is in semitones
        f0_st = hz_to_st(self.series[ 'F0' ])
        f0_shifted = f0_st + x
        self.series[ 'F0' ] = st_to_hz( f0_shifted )
        return
    