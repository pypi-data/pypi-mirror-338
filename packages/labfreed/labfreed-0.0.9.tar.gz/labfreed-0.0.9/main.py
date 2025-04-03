from labfreed.PAC_ID.data_model import IDSegment
from labfreed.PAC_ID.parse import PAC_Parser
from labfreed.TREX.data_model import *
from labfreed.DisplayNameExtension.DisplayNameExtension import DisplayNames
from labfreed.TREX.parse import TREX_Parser, _from_trex_string
from labfreed.validation import LabFREEDValidationError



if __name__ == "__main__":
    # extension_interpreters = {
    #         'TREX': TREX,
    #         'N': DisplayNames
    # }

    # pacid_str = 'HTTPS://PAC.METTORIUS.COM/-DR/AB378/-MD/B-500/1235/-MS/AB/X:88/WWW/-MS/240:11/BB*E4BLEW6R5EVD7XMGHG11*A$HUR:25+B$CEL:99*BLUBB$TREX/A$HUR:25+B$CEL:99'
    # pac = PAC_Parser(extension_interpreters).parse_pac(pacid_str)
    # a=1
    parser = TREX_Parser(suppress_errors=True)
    
    tab = 'TAB$$C0$T.A:C1$T.B::-AB:TRUE::-BB:T' #element (0,1) has wrong type. should be boolean (T or F) but is text 
    trex = parser.parse_trex_str(tab, name='A')
    msg = trex.get_nested_validation_messages()
    
    tab = 'TAB$$C0$T.A:C1$T.B:C2$C63::A:T::B:T:1' # character £ in key
    trex = parser.parse_trex_str(tab, name='A')
    
    st = 'TAB$$AB£$T.AB::AB::BaC:F'
    trex2 = parser.parse_trex_str(st, name='SUM')
    
    st = 'TAB$$A$T.A:B$T.B::AB:T::BaC:F'
    trex2 = parser.parse_trex_str(st, name='SUM')
    
    st = 'TAB$$A$T.A:B$T.B::AB::BaC:F'
    trex2 = parser.parse_trex_str(st, name='SUM')
    

    
    b = [
        'a', '£', '<', 'ABCDeFGh'
    ]
    for e in b:
        trex = parser.parse_trex_str(f'A$E:{e}', name='A')
    
    
    b = [
        'a', '£', '+', '<', 'ABCDeFGh'
    ]
    for e in b:
        trex = parser.parse_trex_str(f'A$T.B:{e}', name='A')
    
    b = [
        '1', '0', 'TRUE', 'FALSE'
    ]
    for e in b:
        trex = parser.parse_trex_str(f'A$T.B:{e}', name='A')
    
    dates = [
        '2024131', '20240000'
    ]
    for e in dates:
        trex = parser.parse_trex_str(f'A$T.D:{e}', name='A')
    
    dates = [
        '20240305'
    ]
    for e in dates:
        trex = parser.parse_trex_str(f'A$T.D:{e}', name='a')
        assert not trex.get_nested_validation_messages()
    
    
    trex_str ='TIME$HUR:A'
    trex = parser.parse_trex_str(trex_str, name="A")
    m = trex.get_nested_validation_messages()
    
    trex_str ='TIME$HUR:25.0'
    trex = parser.parse_trex_str(trex_str, name="A")
    
    trex_str ='TIME$HUR:25'
    trex = parser.parse_trex_str(trex_str, name="A")
    
    trex_str ='TIME$HUR:-25.0'
    trex = parser.parse_trex_str(trex_str, name="A")
    
    trex_str ='TIME$HUR:-25'
    trex = parser.parse_trex_str(trex_str, name="A")
    
    
    
    trex_str = '£TiMe$HUR:1'
    trex = parser.parse_trex_str(trex_str, name="A")

    AlphanumericSegment(value='BB', key='AB', type='T.A')
    sA2 = AlphanumericSegment(key="TMP", value='BCaa')
    m = sA2.get_nested_validation_messages()
    
    #sT2 = TREX_Table2(key='QWE',col_names=['AB', 'CD'], col_types=['T.A', 'T.B'], data=[[AlphanumericValue2(value='ABC')]])


    # sN = ValueSegment2(key='TM', type='HUR', value='1.1')
    # sD = ValueSegment2(key='M', type='T.D', value='20240203')
    # sT = ValueSegment2(key='A', type='T.T', value='ABCD345')
    # A = AlphanumericValue2('ABC')
    # sA = ValueSegment2(key="TMP", type='T.A', value='ABC')
    # sB = ValueSegment2(key="TMP2", type='T.B', value='T')
    # sT = TREX_Table(key='QWE',col_names=['AB', 'CD'], col_types=['T.A', 'T.B'], data=[['A', 'B']])
    # trex = TREX(name_='SUM', segments=[sA, sB, sT])
    
    

    
    s = "P$T.A:VP+O$T.A:VO"
    trex2 = parser.parse_trex_str(s, name='SUM')
    
    try:
        s = "P$T.A:VaP+O$T.A:VaO"
        trex2 = parser.parse_trex_str(s, name='SUM')
    except:
        ...
    

    
    k = "abABC$£"
    v = '90ABF'
    ids = IDSegment(raise_exception_on_validation_error=False, key=k, value=v)
    e = ids.get_validation_messages()
    m = ids.get_nested_validation_messages()
    ids.print_validation_messages(f'{k}:{v}')
    
    parser = PAC_Parser()
    invalid_standard_segments = "-MD/240:B-800/21:123abc45"
    pac_url= "HTTPS://PAC.METTORIUS.COM/" + invalid_standard_segments
    pac = parser.parse_pac_url(pac_url)
    pac.print_validation_messages(pac_url)
    
    # try:
    #     ids = IDSegment(raise_exception_on_validation_error=True, key="ab$£", value='90ABF')
    # except ValueError as e:
    #     err = e.errors()
    #     m = e.args[0]
    
    5