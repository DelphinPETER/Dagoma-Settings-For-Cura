'Cet outil permet de copier les fichiers de profil vierge suivant une liste prédéfini de matériaux
'et de corriger dans chaque fichier le nom du matériau correspondant et le nom de l'imprimante
Option explicit

Const ForReading = 1    
Const ForWriting = 2
Dim printName
printName = "discovery200"

'Défini la liste des matériaux à créer
Dim materialList : Set materialList = CreateObject("System.Collections.ArrayList")
materialList.add("filo3d_pla")
materialList.add("chromatik_pla")
materialList.add("octofiber_pla")
materialList.add("polyplus_pla")
materialList.add("polymax_pla")
materialList.add("polyflex_pla")
materialList.add("other_pla")

'Défini la liste des qualités disponible
Dim qualityList : Set qualityList = CreateObject("System.Collections.ArrayList")
qualityList.add(printName+"_MATERIAU_fin.inst.cfg")
qualityList.add(printName+"_MATERIAU_rapide.inst.cfg")
qualityList.add(printName+"_MATERIAU_standard.inst.cfg")

'Fichier en cour de lecture
Dim strText

'fileSystem
Dim filesys
Set filesys=CreateObject("Scripting.FileSystemObject")

'créer le dossier de destination, s'il existe on le supprime et on le recréait
Dim folderDestination
folderDestination = "dagoma_"+printName
If filesys.FolderExists(folderDestination) Then    
    filesys.deleteFolder(folderDestination)   
End if 
filesys.CreateFolder(folderDestination)

'On boucle l'ouverture des différentes qualités d'impression
Dim qualitySourceFile
For Each qualitySourceFile In qualityList
    
    'Ouverture du fichier source
    Dim objFile
    Set objFile = filesys.OpenTextFile(qualitySourceFile, ForReading)
    strText = objFile.ReadAll
    objFile.Close
    
    'On boucle pour chaque matériau disponible
    Dim materialName
    For Each materialName In materialList
        'On créai le fichier
        call CreateFile(qualitySourceFile, materialName)
    Next
    
Next

'Creation du fichier
Sub CreateFile(ByVal qualitySourceFile, ByVal materialName)    
    
    
    'Creation du nouveau fichier
    Dim newFileName
    newFileName = Replace(qualitySourceFile,"MATERIAU",materialName)
    newFileName = "dagoma_"+ printName + "\" + newFileName
    filesys.CopyFile qualitySourceFile, newFileName
    
    'Remplacement du nom de l'imprimante
    Dim strNewQualityText
    strNewQualityText = strText
    strNewQualityText = Replace(strNewQualityText, "PRINTNAME", printName)

    'Remplacement de la variable par la nom du materiau
    strNewQualityText = Replace(strNewQualityText, "MATERIAU", materialName)      
    
    'Ecriture dans fichier de destination 
    Dim objFile
    Set objFile = filesys.OpenTextFile(newFileName, ForWriting)
    objFile.Write strNewQualityText  'WriteLine adds extra CR/LF
    objFile.Close
    
End Sub