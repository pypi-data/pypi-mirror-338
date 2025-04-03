from dataclasses import dataclass
from enum import Enum
from typing import Union, Optional

Command = Union["ACommand", "LCommand", "CCommand"]


@dataclass(frozen=True)
class ACommand:
    raw_address: Optional[str] = None
    symbol_address: Optional[str] = None
    
    def __post_init__(self) -> None:
        if (self.raw_address is None and self.symbol_address is None) or \
           (self.raw_address is not None and self.symbol_address is not None):
            raise ValueError("Exactly one of 'rawAddress' or 'symbolicAddress' must be provided, not none or both.")
        if self.raw_address is not None and not self.raw_address.isdigit():
            raise ValueError("Raw Address must be a number")
        

@dataclass(frozen=True)
class LCommand:
    label: str


@dataclass(frozen=True)
class CCommand:
    dest: "Dest"
    comp: "Comp"
    jump: "Jump"


class CommandType(Enum):
    A_COMMAND = 1
    C_COMMAND = 2
    L_COMMAND = 3


class Dest(Enum):
    Null = "null"
    M = "M"
    D = "D"
    MD = "MD"
    A = "A"
    AM = "AM"
    AD = "AD"
    AMD = "AMD"


class Jump(Enum):
    Null = "null"
    JGT = "JGT"
    JEQ = "JEQ"
    JGE = "JGE"
    JLT = "JLT"
    JNE = "JNE"
    JLE = "JLE"
    JMP = "JMP"


class PredefinedLabel(Enum):
    SP = "SP"
    LCL = "LCL"
    ARG = "ARG"
    THIS = "THIS"
    THAT = "THAT"
    R0 = "R0"
    R1 = "R1"
    R2 = "R2"
    R3 = "R3"
    R4 = "R4"
    R5 = "R5"
    R6 = "R6"
    R7 = "R7"
    R8 = "R8"
    R9 = "R9"
    R10 = "R10"
    R11 = "R11"
    R12 = "R12"
    R13 = "R13"
    R14 = "R14"
    R15 = "R15"
    SCREEN = "SCREEN"
    KBD = "KBD"


class Comp(Enum):
    zero = "0"  # 0 was not possible
    one = "1"  # 1 was not possible
    minus_one = "-1"
    d = "D"
    a = "A"
    not_d = "!D"
    not_a = "!A"
    minus_d = "-D"
    minus_a = "-A"
    d_plus_1 = "D+1"
    a_plus_1 = "A+1"
    d_minus_1 = "D-1"
    a_minus_1 = "A-1"
    d_plus_a = "D+A"
    d_minus_a = "D-A"
    a_minus_d = "A-D"
    d_and_a = "D&A"
    d_or_a = "D|A"
    m = "M"
    not_m = "!M"
    minus_m = "-M"
    m_plus_1 = "M+1"
    m_minus_1 = "M-1"
    d_plus_m = "D+M"
    d_minus_m = "D-M"
    m_minus_d = "M-D"
    d_and_m = "D&M"
    d_or_m = "D|M"
