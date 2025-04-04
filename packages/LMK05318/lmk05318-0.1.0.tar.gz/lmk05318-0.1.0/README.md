# Linux pure Python library for LMK05318 Ultra-Low Jitter Network Synchronizer Clock With Two Frequency Domains.

By default the address is **0x64**. Check the device is present in your system (I2C bus **0** in our case):
```
# i2cdetect -y 0
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         08 -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- UU -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- UU -- -- -- 
50: -- -- UU UU -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- 64 -- -- -- -- UU -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --
```
Run `test.py` to see if everything works:
```
from lmk05318 import LMK05318
from ti_i2c_regs import lmk_i2c_regs
import logging
def main():
    lmk_regs_iface = lmk_i2c_regs(0, 0x64)
    lmk = LMK05318(regs_iface=lmk_regs_iface)

    vendor_id = lmk.get_vendor_id()
    print(f"LMK05318 vendor_id: {hex(vendor_id)}")

    status = lmk.get_status_dpll()
    print(f"LMK05318 status {status}")

    valid = lmk.is_chip_id_valid()
    print(f"LMK05318 valid: {valid}")
    lmk.write_cfg_regs_to_eeprom(LMK05318.LMK_EEPROM_REG_COMMIT)

    vendor_id = lmk.get_vendor_id()
    print(f"LMK05318 vendor_id: {hex(vendor_id)}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()

```

# Debug and development

Copy the tarball with Python sources to your board */tmp* directory:
```
./copy_to_board.sh 192.168.2.21
```

Run on board as root:
```
cd /tmp && ./untar_install.sh LMK05318
```

Run test.py as root:
```
root@xxx:/tmp# python3 LMK05318/test.py
INFO:lmk05318:Vendor ID Readback: 0x100B
LMK05318 vendor_id: 0x100b
LMK05318 status 
        Loss of phase lock: 1
        Loss of freq. lock: 1
        Tuning word update: 0
        Holdover Event: 1
        Reference Switch Event: 0
        Active ref. missing clk: 0
        Active ref. loss freq.: 0
        Active ref. loss ampl.: 0
        
INFO:lmk05318:Vendor ID Readback: 0x100B
INFO:lmk05318:Product ID Readback: 0x35
LMK05318 valid: True
INFO:lmk05318:write current device register content to EEPROM
INFO:lmk05318:wait till busy bit becomes 1
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:wait till busy bit becomes 0
INFO:lmk05318:programming EEPROM done, power-cycle or hard-reset to take effect
INFO:lmk05318:Vendor ID Readback: 0x100B
LMK05318 vendor_id: 0x100b

```