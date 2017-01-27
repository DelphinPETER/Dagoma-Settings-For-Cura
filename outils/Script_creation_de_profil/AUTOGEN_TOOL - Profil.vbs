'Cet outil permet de copier les fichiers de profil vierge suivant une liste prédéfini de matrériaux
'et de corriger dans chaque fichier le nom du matériau correspondant


Const ForReading = 1    
Const ForWriting = 2

'Défini la liste des matériaux à créer
Dim materialList : Set materialList = CreateObject("System.Collections.ArrayList")
materialList.add("chromatik_pla")
materialList.add("fiberlogy_hd_pla")
materialList.add("filo3d_green_pla")
materialList.add("filo3d_pla")
materialList.add("filo3d_red_pla")
materialList.add("octofiber_pla")
materialList.add("other_pla")
materialList.add("polyflex_pla")
materialList.add("polymax_pla")
materialList.add("polyplus_pla")
materialList.add("polywood_pla")

'Défini la liste des qualités disponible
Dim qualityList : Set qualityList = CreateObject("System.Collections.ArrayList")
qualityList.add("AUTOGEN_fin.inst.cfg")
qualityList.add("AUTOGEN_rapide.inst.cfg")
qualityList.add("AUTOGEN_standard.inst.cfg")

Dim strText'Fichier en cour de lecture

'On boucle l'ouverture des différentes qualités d'impression
For Each qualitySourceFile In qualityList

    'Ouverture du fichier source
    Set objFSO = CreateObject("Scripting.FileSystemObject")
    Set objFile = objFSO.OpenTextFile(qualitySourceFile, ForReading)
    strText = objFile.ReadAll
    objFile.Close
    
    'On boucle pour chaque matériau disponible
    For Each materialName In materialList
        'On créai le fichier
        call CreateFile(qualitySourceFile, materialName)
    Next
    
Next

'Creation du fichier
Sub CreateFile(ByVal qualitySourceFile, ByVal materialName)
    
    'Creation du nouveau fichier
    newFileName = Replace(qualitySourceFile,"AUTOGEN",materialName)
    Set filesys=CreateObject("Scripting.FileSystemObject")
    filesys.CopyFile qualitySourceFile, newFileName    
    
    'Remplacement de la valeur generique par la nom du materiau
    strNewQualityText = Replace(strText, "AUTOGEN", materialName)
    
    'Ecriture dans fichier de destination
    Set objFile = objFSO.OpenTextFile(newFileName, ForWriting)
    objFile.Write strNewQualityText  'WriteLine adds extra CR/LF
    objFile.Close
    
End Sub