import os
import io

from abundance.banner.AbundanceBanner import AbundanceBanner
from PIL import Image

class AbundanceApplicationBannerPrinter:
    BANNER_LOCATION_PROPERTY = "abundance.banner.location"
    BANNER_IMAGE_LOCATION_PROPERTY = "abundance.banner.image.path"
    DEFAULT_BANNER_LOCATION = "resources"
    DEFAULT_BANNER_NAME = "banner.txt"
    IMAGE_EXTENSION = ["gif", "jpg", "png", "jpeg"]
    DEFAULT_BANNER = AbundanceBanner()  # 这里假设你有对应的默认横幅实现，比如一个简单的文本横幅类，暂设为None

    def __init__(self, resource_loader, fallback_banner):
        self.resource_loader = resource_loader
        self.fallback_banner = fallback_banner

    def print(self, environment, logger):
        banner = self.get_banner(environment)
        try:
            self.create_string_from_banner(banner, logger)
        except UnicodeDecodeError as e:
            logger.warn(f"Failed to create String for banner: {e}")

    def get_banner(self, environment):
        banners = Banners()
        image_banner = self.get_image_banner(environment)
        text_banner = self.getText_banner(environment)
        banners.add_if_not_null(image_banner)
        banners.add_if_not_null(text_banner)
        if banners.has_at_least_one_banner():
            return banners
        return self.fallback_banner if self.fallback_banner else self.DEFAULT_BANNER

    def getText_banner(self, environment):
        location = environment.get(self.BANNER_LOCATION_PROPERTY)
        if location:
            resource = self.resource_loader.get_resource(location)
            if resource.exists():
                return ResourceBanner(resource)
        resource = self.resource_loader.get_resource(os.path.join(self.DEFAULT_BANNER_LOCATION, self.DEFAULT_BANNER_NAME))
        if resource.exists():
            return ResourceBanner(resource)
        return None

    def get_image_banner(self, environment):
        location = environment.get(self.BANNER_IMAGE_LOCATION_PROPERTY)
        if location:
            resource = self.resource_loader.get_resource(location)
            if resource.exists():
                return ImageBanner(resource)
            return None
        for ext in self.IMAGE_EXTENSION:
            resource = self.resource_loader.get_resource(os.path.join(self.DEFAULT_BANNER_LOCATION, f"banner.{ext}"))
            if resource.exists():
                return ImageBanner(resource)
        return None

    def create_string_from_banner(self, banner, logger):
        banner.print_banner(logger)

class Banners:
    def __init__(self):
        self.banners = []

    def add_if_not_null(self, banner):
        if banner:
            self.banners.append(banner)

    def has_at_least_one_banner(self):
        return len(self.banners) > 0

    def print_banner(self, out):
        for banner in self.banners:
            banner.print_banner(out)

class ResourceBanner:
    def __init__(self, resource):
        self.resource = resource

    def print_banner(self, out):
        out(self.resource.get.decode('utf-8'))


class ImageBanner:
    def __init__(self, resource):
        self.resource = resource

    def print_banner(self, out):
        try:
            width = 60
            # 将二进制数据转换为图像对象
            image = Image.open(io.BytesIO(self.resource.get))
            # 调整图片大小
            aspect_ratio = image.height / image.width
            height = int(width * aspect_ratio)
            new_image = image.resize((width, height))
            # 将图片转换为灰度图
            new_image = new_image.convert('L')
            pixels = new_image.getdata()
            # 定义 ASCII 字符集，用于替换像素值
            chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
            new_pixels = [chars[pixel // 25] for pixel in pixels]
            new_pixels = ''.join(new_pixels)
            # 将字符按宽度分割成多行
            ascii_image = [new_pixels[index:index + width] for index in range(0, len(new_pixels), width)]
            banner = '\n'.join(ascii_image)
            out(banner)
        except Exception as e:
            print(f"转换过程中出现错误: {e}")







