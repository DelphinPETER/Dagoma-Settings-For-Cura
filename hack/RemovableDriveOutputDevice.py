# Copyright (c) 2016 Ultimaker B.V.
# Cura is released under the terms of the AGPLv3 or higher.

import os.path

from UM.Application import Application
from UM.Logger import Logger
from UM.Message import Message
from UM.FileHandler.WriteFileJob import WriteFileJob
from UM.Mesh.MeshWriter import MeshWriter
from UM.Scene.Iterator.BreadthFirstIterator import BreadthFirstIterator
from UM.OutputDevice.OutputDevice import OutputDevice
from UM.OutputDevice import OutputDeviceError

from UM.i18n import i18nCatalog
catalog = i18nCatalog("cura")

class RemovableDriveOutputDevice(OutputDevice):
    def __init__(self, device_id, device_name):
        super().__init__(device_id)

        self.setName(device_name)
        self.setShortDescription(catalog.i18nc("@action:button Preceded by 'Ready to'.", "Save to Removable Drive"))
        self.setDescription(catalog.i18nc("@item:inlistbox", "Save to Removable Drive {0}").format(device_name))
        self.setIconName("save_sd")
        self.setPriority(1)

        self._writing = False
        self._stream = None

    ##  Request the specified nodes to be written to the removable drive.
    #
    #   \param nodes A collection of scene nodes that should be written to the
    #   removable drive.
    #   \param file_name \type{string} A suggestion for the file name to write
    #   to. If none is provided, a file name will be made from the names of the
    #   meshes.
    #   \param limit_mimetypes Should we limit the available MIME types to the
    #   MIME types available to the currently active machine?
    #
    def requestWrite(self, nodes, file_name = None, filter_by_machine = False, file_handler = None, **kwargs):
        filter_by_machine = True # This plugin is indended to be used by machine (regardless of what it was told to do)
        if self._writing:
            raise OutputDeviceError.DeviceBusyError()

        # Formats supported by this application (File types that we can actually write)
        if file_handler:
            file_formats = file_handler.getSupportedFileTypesWrite()
        else:
            file_formats = Application.getInstance().getMeshFileHandler().getSupportedFileTypesWrite()

        if filter_by_machine:
            container = Application.getInstance().getGlobalContainerStack().findContainer({"file_formats": "*"})

            # Create a list from supported file formats string
            machine_file_formats = [file_type.strip() for file_type in container.getMetaDataEntry("file_formats").split(";")]

            # Take the intersection between file_formats and machine_file_formats.
            file_formats = list(filter(lambda file_format: file_format["mime_type"] in machine_file_formats, file_formats))

        if len(file_formats) == 0:
            Logger.log("e", "There are no file formats available to write with!")
            raise OutputDeviceError.WriteRequestFailedError()

        # Just take the first file format available.
        if file_handler is not None:
            writer = file_handler.getWriterByMimeType(file_formats[0]["mime_type"])
        else:
            writer = Application.getInstance().getMeshFileHandler().getWriterByMimeType(file_formats[0]["mime_type"])

        extension = file_formats[0]["extension"]

        if file_name is None:
            file_name = self._automaticFileName(nodes)

        if extension:  # Not empty string.
            extension = "." + extension
        #file_name = os.path.join(self.getId(), os.path.splitext(file_name)[0] + extension)
        file_name = os.path.join(self.getId(), "dagoma0.g")

        try:
            Logger.log("d", "Writing to %s", file_name)
            # Using buffering greatly reduces the write time for many lines of gcode
            self._stream = open(file_name, "wt", buffering = 1, encoding = "utf-8")
            job = WriteFileJob(writer, self._stream, nodes, MeshWriter.OutputMode.TextMode)
            job.setFileName(file_name)
            job.progress.connect(self._onProgress)
            job.finished.connect(self._onFinished)

            message = Message(catalog.i18nc("@info:progress", "Saving to Removable Drive <filename>{0}</filename>").format(self.getName()), 0, False, -1)
            message.show()

            self.writeStarted.emit(self)

            job.setMessage(message)

            self._writing = True
            job.start()
        except PermissionError as e:
            Logger.log("e", "Permission denied when trying to write to %s: %s", file_name, str(e))
            raise OutputDeviceError.PermissionDeniedError(catalog.i18nc("@info:status", "Could not save to <filename>{0}</filename>: <message>{1}</message>").format(file_name, str(e))) from e
        except OSError as e:
            Logger.log("e", "Operating system would not let us write to %s: %s", file_name, str(e))
            raise OutputDeviceError.WriteRequestFailedError(catalog.i18nc("@info:status", "Could not save to <filename>{0}</filename>: <message>{1}</message>").format(file_name, str(e))) from e

    ##  Generate a file name automatically for the specified nodes to be saved
    #   in.
    #
    #   The name generated will be the name of one of the nodes. Which node that
    #   is can not be guaranteed.
    #
    #   \param nodes A collection of nodes for which to generate a file name.
    def _automaticFileName(self, nodes):
        for root in nodes:
            for child in BreadthFirstIterator(root):
                if child.getMeshData():
                    name = child.getName()
                    if name:
                        return name
        raise OutputDeviceError.WriteRequestFailedError("Could not find a file name when trying to write to {device}.".format(device = self.getName()))

    def _onProgress(self, job, progress):


        self.writeProgress.emit(self, progress)

    def _onFinished(self, job):
        if self._stream:
            # Explicitly closing the stream flushes the write-buffer
            self._stream.close()
            self._stream = None





        self._writing = False
        self.writeFinished.emit(self)
        if job.getResult():
            message = Message(catalog.i18nc("@info:status", "Saved to Removable Drive {0} as {1}").format(self.getName(), os.path.basename(job.getFileName())))
            message.addAction("eject", catalog.i18nc("@action:button", "Eject"), "eject", catalog.i18nc("@action", "Eject removable device {0}").format(self.getName()))
            message.actionTriggered.connect(self._onActionTriggered)
            message.show()
            self.writeSuccess.emit(self)
        else:
            message = Message(catalog.i18nc("@info:status", "Could not save to removable drive {0}: {1}").format(self.getName(), str(job.getError())))
            message.show()
            self.writeError.emit(self)
        job.getStream().close()

    def _onActionTriggered(self, message, action):
        if action == "eject":
            if Application.getInstance().getOutputDeviceManager().getOutputDevicePlugin("RemovableDriveOutputDevice").ejectDevice(self):
                message.hide()

                eject_message = Message(catalog.i18nc("@info:status", "Ejected {0}. You can now safely remove the drive.").format(self.getName()))
            else:
                eject_message = Message(catalog.i18nc("@info:status", "Failed to eject {0}. Another program may be using the drive.").format(self.getName()))
            eject_message.show()
