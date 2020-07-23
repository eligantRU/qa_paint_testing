class Ribbon:
	class ImageGroup:
		__parent = None

		def __init__(self, parent):
			self.__parent = parent

		def __call__(self, *args, **kwargs):
			return self.__parent.child_window(title="Изображение", control_type="ToolBar")

		def change_size(self):
			return self().child_window(title="Изменить размер", control_type="Button")

	__ppt = None

	def __init__(self, ppt):
		self.__ppt = ppt

	def __call__(self, *args, **kwargs):
		return self.__ppt.child_window(title="Главная", control_type="Custom")

	def image(self):
		return Ribbon.ImageGroup(self())
