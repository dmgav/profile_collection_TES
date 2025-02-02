from bluesky.suspenders import SuspendFloor, SuspendBoolHigh, SuspendCeil
import bluesky.plan_stubs as bps

#ring_suspender = SuspendFloor(ring_curr, 190, resume_thresh=400, sleep=300)#,
                              #post_plan=beamline_align_v3_for_suspenders)

#shutterb_suspender = SuspendBoolHigh(EpicsSignalRO(shutterb.status.pvname), sleep=300)#,
									 #post_plan=beamline_align_v3_for_suspenders)

# Is this the right PV???
#fe_shut_suspender = SuspendBoolHigh(EpicsSignal('XF:02ID-PPS{Sh:FE}Pos-Sts'), sleep=300)
#fe_shut_suspender = SuspendBoolHigh(EpicsSignal('XF:02ID-PPS{Sh:FE}Pos-Sts'), sleep=10*60)

## It needs:
## RE.install_suspender(test_shutsusp)
## RE.remove_suspender(test_shutsusp)

#RE.install_suspender(ring_suspender)
#RE.install_suspender(fe_shut_suspender)
#RE.install_suspender(shutterb_suspender)


'''
ring_current = EpicsSignal('SR:OPS-BI{DCCT:1}I:Real-I')
sus = SuspendFloor(ring_current, 100, resume_thresh=400, sleep=600)
RE.install_suspender(sus)

absorber_pos = EpicsSignal( 'XF:11BMB-ES{SM:1-Ax:ArmR}Mtr.RBV')
sus_abs_low = SuspendFloor(absorber_pos, -56, resume_thresh=-55)
sus_abs_hi = SuspendCeil(absorber_pos, -54, resume_thresh=-55)
RE.install_suspender(sus_abs_low)
RE.install_suspender(sus_abs_hi)

'''

ring_current = EpicsSignal('SR:OPS-BI{DCCT:1}I:Real-I')
ring_suspender = SuspendFloor(ring_current, 190, resume_thresh=390, sleep=60)
#                              post_plan=beamline_align_suspenders)

solenoid_v = EpicsSignal('XF:08BMES-BI{PSh:1-BPM:4}V-I')
I0 = EpicsSignal("XF:08BM-ES{IO:2}AI:1-I")
H_feedback_top = EpicsSignal('XF:08BM-ES{IO:2}AI:2-I')
H_feedback_bottom = EpicsSignal('XF:08BM-ES{IO:2}AI:3-I')

solenoid_v_suspenderCeil = SuspendCeil(solenoid_v, 0.3, resume_thresh = 0.05, sleep = 10,
                                       #post_plan = mono_tilt
                                       )
solenoid_v_suspenderFloor = SuspendFloor(solenoid_v, -0.3, resume_thresh = -0.05, sleep = 10,
                                       #post_plan = mono_tilt
                                       )

I0_suspenderFloor = SuspendFloor(I0, 0.02, resume_thresh= 0.1, sleep = 2)
RE.install_suspender(ring_suspender)
#RE.install_suspender(solenoid_v_suspenderCeil)
#RE.install_suspender(solenoid_v_suspenderFloor)
RE.install_suspender(I0_suspenderFloor)


'''

def mono_tilt():
    H_Top = H_feedback_top.value
    sole_v = solenoid_v.value
    direction = 1
    while H_feedback_top.value > 0.05 and abs(solenoid_v.value) > 0.15:
        yield from bps.mv(mono.tilt, mono.tilt.position + direction*5)
        yield from bps.sleep(1)
        if H_feedback_top.value - H_Top >=0 or abs(solenoid_v.value) - abs(sole_v) <=0:
            direction = 1
            
   
   
        
'''
'''
        
        if solenoid_v.value >= 0.3 && solenoid_v.value <=0.33:
            bps.mv(mono.tilt, mono.tilt.position+5)
            yield from bps.sleep(1)
        elif solenoid_v.value <= -0.3 && solenoid_v.value >= -0.33:
            bps.mv(mono.tilt, mono.tilt.position-5)
            yield from bps.sleep(1)
        elif solenoid_v.value <= -0.336:
            bps.mv(mono.tilt, mono.tilt.position+5)
            yield from bps.sleep(1)
         elif solenoid_v.value >= 0.336:
            bps.mv(mono.tilt, mono.tilt.position-5)
            yield from bps.sleep(1)
        else:
            break
'''
