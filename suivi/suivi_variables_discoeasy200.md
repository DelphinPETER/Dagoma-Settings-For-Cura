

Definition des caracteristiques mecaniques

Variables CbD                 | Valeurs       | Variables Cura                 | Fichiers | Vérifié | Commentaire
------------------------------|---------------|--------------------------------|----------|---------|------------
machine_name                  | DiscoEasy200  | machine_name                   | JSON     |  OK     | 
machine_type                  | DiscoEasy200  |                                | JSON     |  OK     | 
machine_width                 | 211           | machine_width                  | JSON     |  OK     | 
machine_depth                 | 211           | machine_depth                  | JSON     |  OK     | 
machine_height                | 205           | machine_height                 | JSON     |  OK     | 
extruder_amount               | 1             | machine_extruder_count         | JSON     |  OK     | 
has_heated_bed                | False         | machine_heated_bed             | JSON     |  OK     | 
machine_center_is_zero        | False         | machine_center_is_zer          | JSON     |  OK     | 
nozzle_size                   | 0.4           | machine_nozzle_size            | JSON     |  OK     | 
extruder_head_size_min_x      | 17            | machine_head_with_fans_polygon | JSON     |  OK     | 
extruder_head_size_min_y      | 40            | machine_head_with_fans_polygon | JSON     |  OK     | 
extruder_head_size_max_x      | 17            | machine_head_with_fans_polygon | JSON     |  OK     | 
extruder_head_size_max_y      | 70            | machine_head_with_fans_polygon | JSON     |  OK     |  
extruder_head_size_height     | 10            | machine_head_with_fans_polygon | JSON     |  OK     | 
gcode_flavor                  | DiscoGCode    | machine_gcode_flavor           | JSON     |  OK     | 
retraction_enable             | True          | retraction_enable              | JSON     |  OK     | 
machine_shape                 | Square        |                                |          |         | 

Definition de la retraction et de la premiere couche

Variables CbD                 | Valeurs       | Variables Cura       | Fichiers | Vérifié | Commentaire
------------------------------|---------------|----------------------|----------|---------|------------
retraction_speed              | 50            | retraction_speed     | JSON     |  OK     | 
retraction_amount             | 3.5           | retraction_amount    | JSON     |  OK     | 
bottom_thickness              | 0.26          | top_bottom_thickness | Profil   |  OK     | Défini par top_bottom_thickness
cool_min_layer_time           | 10            | cool_min_layer_time  | JSON     |  OK     | 
fan_enabled                   | True          | cool_fan_enabled     | JSON     |  OK     | 
layer0_width_factor           | 100           |                      |          |         | VOIR si layer_0_z_overlap avec une opération pour le pourcentage correspond
object_sink                   | 0             |                      |          |         | 

Definition des caracteristiques du support

Variables CbD                    | Valeurs    | Variables Cura                 | Fichiers | Vérifié | Commentaire
---------------------------------|------------|--------------------------------|----------|---------|------------
retraction_min_travel            | 1.5        | retraction_min_travel          | JSON     |  OK     | 
retraction_hop                   | 0          | retraction_hop                 | JSON     |  OK     | 
skirt_line_count                 | 2          | skirt_line_count               | JSON     |  OK     | 
skirt_gap                        | 3          | skirt_gap                      | JSON     |  OK     | 
skirt_minimal_length             | 150        | skirt_brim_minimal_length      | JSON     |  OK     | 
fan_full_height                  | 0.5        | cool_fan_full_at_height        | JSON     |  OK     | 
fan_speed                        | 50         | cool_fan_speed                 | JSON     |  OK     | default_value
fan_speed_max                    | 100        | cool_fan_speed                 | JSON     |  OK     | maximum_value
cool_head_lift                   | False      | cool_lift_head                 | JSON     |  OK     | 
support_type                     | Lines      | support_pattern                | JSON     |  OK     | 
support_angle                    | 50         | support_angle                  | JSON     |  OK     | 
support_fill_rate                | 20         | support_infill_rate            | JSON     |  OK     | 
support_xy_distance              | 0.7        | support_xy_distance            | JSON     |  OK     | 
support_z_distance               | 0.15       | support_z_distance             | JSON     |  OK     | 
spiralize                        | False      | magic_spiralize                | JSON     |  OK     | 
brim_line_count                  | 10         | brim_line_count                | JSON     |  OK     | 
raft_margin                      | 5          | raft_margin                    | JSON     |  OK     |
raft_base_thickness              | 0.3        | raft_base_thickness            | JSON     |  OK     | 
raft_base_linewidth              | 1          | raft_base_line_width           | JSON     |  OK     | 
raft_interface_thickness         | 0.27       | raft_interface_thickness       | JSON     |  OK     | 
raft_interface_linewidth         | 0.4        | raft_interface_line_width      | JSON     |  OK     | 
raft_airgap                      | 0.22       | raft_airgap                    | JSON     |  OK     | 
raft_surface_layers              | 2          | raft_surface_layers            | JSON     |  OK     | 
fix_horrible_union_all_type_a    | True       | meshfix_union_all              | JSON     |  OK     | 
fix_horrible_union_all_type_b    | False      | meshfix_union_all_remove_holes | JSON     |  OK     | 
fix_horrible_use_open_bits       | False      | meshfix_keep_open_polygons     | JSON     |  OK     | 
fix_horrible_extensive_stitching | False      | meshfix_extensive_stitching    | JSON     |  OK     | 

Variables CbD                    | Valeurs    | Variables Cura | Fichiers | Vérifié | Commentaire
---------------------------------|------------|----------------|----------|---------|------------
simple_mode                      | False      |                |          |  OK     | Non utilisé
retraction_combing               | True       |                |          |         | 
retraction_minimal_extrusion     | 0.02       |                |          |         | 
cool_min_feedrate                | 20         |                |          |         | 
solid_top                        | True       |                |          |         | 
solid_bottom                     | True       |                |          |         | 
fill_overlap                     | 25         |                |          |         | 
raft_line_spacing                | 3          |                |          |         |raft_interface_line_spacing 
