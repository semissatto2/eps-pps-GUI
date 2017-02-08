from epics import PV

pvValues = [0]*32
#	Import EPS AI Cat Values
pv1=PV('IVUFE:EPS:AI_UTL-WPR-TT')
pv2=PV('IVUFE:EPS:AI_UTL-WRT-TT')
pv3=PV('IVUFE:EPS:AI_DEV-XBPM1-TT')
pv4=PV('IVUFE:EPS:AI_DEV-XBPM1-TT1')
pv5=PV('IVUFE:EPS:AI_DEV-XBPM1-TT2')
pv6=PV('IVUFE:EPS:AI_DEV-XBPM1-TT3')
pv7=PV('IVUFE:EPS:AI_DEV-XBPM1-TT4')
pv8=PV('IVUFE:EPS:AI_DEV-XBPM2-TT')
pv9=PV('IVUFE:EPS:AI_DEV-XBPM2-TT1')
pv10=PV('IVUFE:EPS:AI_DEV-XBPM2-TT2')
pv11=PV('IVUFE:EPS:AI_DEV-XBPM2-TT3')
pv12=PV('IVUFE:EPS:AI_DEV-XBPM2-TT4')
pv13=PV('IVUFE:EPS:AI_DEV-MSK-TT')
pv14=PV('IVUFE:EPS:AI_DEV-MSK-TT1')
pv15=PV('IVUFE:EPS:AI_DEV-MSK-TT2')
pv16=PV('IVUFE:EPS:AI_DEV-MSK-TT3')
pv17=PV('IVUFE:EPS:AI_DEV-MSK-TT4')
pv18=PV('IVUFE:EPS:AI_DEV-SLITS-TT')
pv19=PV('IVUFE:EPS:AI_DEV-SLITS-TT1')
pv20=PV('IVUFE:EPS:AI_DEV-SLITS-TT2')
pv21=PV('IVUFE:EPS:AI_DEV-SLITS-TT3')
pv22=PV('IVUFE:EPS:AI_DEV-SLITS-TT4')
pv23=PV('IVUFE:EPS:AI_DEV-PS-TT1')
pv24=PV('IVUFE:EPS:AS_UTL-CAR-PIT')
pv25=PV('IVUFE:EPS:AS_UTL-WPR-FIT')
pv26=PV('IVUFE:EPS:AS_UTL-WPR-PIT')
pv27=PV('IVUFE:EPS:AS_UTL-WRT-FIT')
pv28=PV('IVUFE:EPS:AS_UTL-WRT-PIT')
pv29=PV('IVUFE:EPS:AS_DEV-XBPM1-FIT')
pv30=PV('IVUFE:EPS:AS_DEV-XBPM2-FIT')
pv31=PV('IVUFE:EPS:AS_DEV-MSK-FIT')
pv32=PV('IVUFE:EPS:AS_DEV-SLITS-FIT')

#	Read EPS AI Cat Values
pvValues[0]=pv1.value
pvValues[1]=pv2.value
pvValues[2]=pv3.value
pvValues[3]=pv4.value
pvValues[4]=pv5.value
pvValues[5]=pv6.value
pvValues[6]=pv7.value
pvValues[7]=pv8.value
pvValues[8]=pv9.value
pvValues[9]=pv10.value
pvValues[10]=pv11.value
pvValues[11]=pv12.value
pvValues[12]=pv13.value
pvValues[13]=pv14.value
pvValues[14]=pv15.value
pvValues[15]=pv16.value
pvValues[16]=pv17.value
pvValues[17]=pv18.value
pvValues[18]=pv19.value
pvValues[19]=pv20.value
pvValues[20]=pv21.value
pvValues[21]=pv22.value
pvValues[22]=pv23.value
pvValues[23]=pv24.value
pvValues[24]=pv25.value
pvValues[25]=pv26.value
pvValues[26]=pv27.value
pvValues[27]=pv28.value
pvValues[28]=pv29.value
pvValues[29]=pv30.value
pvValues[30]=pv31.value
pvValues[31]=pv32.value

#print (pvValues)	# Debbug