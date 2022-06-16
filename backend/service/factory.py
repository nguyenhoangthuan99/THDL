from .ToanMathService import ToanMathService
from .OnluyenService import OnluyenService
from .TracNghiemService import TracNghiemService
FACTORY = {"toanmath":ToanMathService,
           "onluyen":OnluyenService,
           "tracnghiem":TracNghiemService}