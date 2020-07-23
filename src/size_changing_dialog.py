class SizeChangingDialog:
	__parent = None

	def __init__(self, parent):
		self.__parent = parent

	def __call__(self, *args, **kwargs):
		return self.__parent.child_window(title="Изменение размеров и наклона", control_type="Window")

	def apply(self):
		return self().child_window(title="ОК", auto_id="1", control_type="Button")

	def vertical_size(self):
		return self().child_window(title="По вертикали:", auto_id="1020", control_type="Edit")
