import PyPDF2
f=open('Working_Business_Proposal.pdf','rb')
pdf_read=PyPDF2.PdfFileReader(f)
first_page=pdf_read.getPage(0)
pdf_writer=PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)
pdf_output=open('Some_New_Doc.pdf','rb')
f.close()
pdf_output.close()