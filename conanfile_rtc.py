from conans import ConanFile

class VulkanUtilityLibrariesConan(ConanFile):
    name = "Vulkan-Utility-Libraries"
    version = "0.0.1"
    url = "https://github.com/duncanthomson/Vulkan-Utility-Libraries"
    license = "https://github.com/duncanthomson/Vulkan-Utility-Libraries/blob/main/LICENSES/Apache-2.0.txt"
    description = "Share code across various Vulkan repositories, solving long standing issues for Vulkan SDK developers and users"

    # RTC specific triple
    settings = "platform_architecture_target"

    def package(self):
        base = self.source_folder
        relative = "3rdparty/Vulkan-Utility-Libraries"

        # headers
        self.copy("*.h", src=base + "/include", dst=relative + "/include")
        self.copy("*.hpp", src=base + "/include", dst=relative + "/include")

        # libraries
        # Only headers are required by RTC, at present: no library
