class Composite(object):	
	def __init__(self):
		self._children =	list()

	def add(self,element):
		self._children.append(element)

	def get_children(self):
		return self._children;


class Book(Composite):
	def __init__(self,title):
		super(Book,self).__init__()
		self._title = title

	def get_title(self):
		return self._title

	def __str__(self):

		val = "+"+self.get_title()+"\n"

		for child in self._children:
			val+="\t"+str(child)

		return val

	
class Chapter(Composite):
	def __init__(self,title):
		super(Chapter,self).__init__()
		self._title = title

	def get_title(self):
		return self._title

	def __str__(self):
		val = " +"+self._title+"\n"

		for child in self._children:
			val+="\t\t"+str(child)+"\n"

		return val

class Paragraph(Composite):
	def __init__(self,text):
		super(Paragraph,self).__init__()
		self._text = text

	def get_text(self):
		return self._text

	def __str__(self):
		return self._text





book = Book('Testing composite')

chapter1 = Chapter('1: Using composite to try things')

par1 = Paragraph('This is lame')
chapter1.add(par1)

chapter2 = Chapter('2: This one is lamer')


book.add(chapter1)
book.add(chapter2)

print str(book)