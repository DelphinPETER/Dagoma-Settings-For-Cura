## Vous possédez un imprimante 3D de chez DAGOMA et vous désirez passer de CuraByDagoma à Cura 2.3.
Voici les fichiers qui vous permettront de retrouver les paramètres par défaut de CuraByDagoma dans Cura version 2.3

Les fichiers sont à copier dans le dossier d'installation de Cura.

Par défaut, sous Windows 64bits :
`C:\Program Files\Cura 2.3`

- Les paramètres de l'imprimante :
  - `.\resources\definitions\dagoma_discoeasy.def.json`
- Le modèle 3D de l'imprimante :
  - `.\resources\meshes\dagoma_discoeasy200_plateform.STL`
- Les paramètres de qualité d'impression :
  - `.\resources\quality\fin.inst.cfg`
  - `.\resources\quality\rapide.inst.cfg`
  - `.\resources\quality\standard.inst.cfg`
- Les paramètres des différents filaments :
  - `.\resources\materials\*.xml.fdm_material`

**Attention ces fichiers vous sont fournis sans garantie**. Je ne pourrais être tenu responsable d'un quelconque dommage causé à votre imprimante 3D. A vous de bien vérifier les paramètres avant de lancer l'impression.

##ASTUCE :

Si vous souhaitez accélérer le chargement de Cura, vous pouvez supprimer les imprimantes que vous n'utilisez pas.
`.\resources\definitions\*.def.json`**SAUF fdmprinter.def.json**
