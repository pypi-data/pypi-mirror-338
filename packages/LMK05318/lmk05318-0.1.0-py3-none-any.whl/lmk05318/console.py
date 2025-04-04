from lmk05318 import LMK05318
from ti_i2c_regs import lmk_i2c_regs
def main():
    lmk_regs_iface = lmk_i2c_regs(0, 0x64)
    lmk = LMK05318(regs_iface=lmk_regs_iface)
    vendor_id = lmk.get_vendor_id()
    print(f"LMK05318 vendor_id: {hex(vendor_id)}")
    status = lmk.get_status_dpll()
    print(f"LMK05318 status {status}")
    valid = lmk.is_chip_id_valid()
    print(f"LMK05318 valid: {valid}")
if __name__ == '__main__':
    main()