import unreal

#define actor location
actorLocation = unreal.Vector(0, 0, 0)
actorRotation = unreal.Rotator(0, 0, 0)
levelSubsystem = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

#create new atmospheric actors
dirLight = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.DirectionalLight, actorLocation, actorRotation)
skyLight = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.SkyLight, actorLocation, actorRotation)
sky = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.SkyAtmosphere, actorLocation, actorRotation)
fog = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.ExponentialHeightFog, actorLocation, actorRotation)
clouds = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.VolumetricCloud, actorLocation, actorRotation)

#save level with atmospherics
levelSubsystem.save_current_level()
