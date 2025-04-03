from pylatex import (Document, Package, Command, NewPage, Tabularx
                     #Section, Subsection, Subsubsection, Itemize,  HorizontalSpace, Description, Marker
                    )

#from pylatex.section import Paragraph, Chapter
from pylatex.utils import (#italic, 
                           NoEscape)
from ..report import Markdown, CurrentContainer, ReportText, IPMarkdown, ObjectCode,display
from ..components.mech import en as mech_comp
from ..components.guides import en as guide_comp
from ..components.ode import pl as ode_comp

from ..components.guides.reporting import en as reporting_comp
from ..components.guides.github import en as github_comp
from ..components.guides.systems import en as systems_comp
from ..components.guides.development import en as development_comp
from ..components.guides.pandas import en as pandas_comp
from typing import Optional, List, Union

#from sympy import *
import datetime

class ReportMethods:

    _reported_object = None
    
    @classmethod
    def base_setup(cls):
        
        preliminary_str=(
"""

Examplary setup is as follows:

## CELL 1
## Imports



    from dynpy.utilities.report import *
    from dynpy.utilities.templates.document import Guide

    doc = Guide('./output/report_name')
    

## CELL 2
## Text reporting
    
    #!!! BE SURE ALL PREVIOUS CELLS ARE RUN !!!#
    #!!!       BECAUSE OF NEEDED IMPORTS    !!!#
    
    sec_text = Section('Section that presents text reporting')
    CurrentContainer(sec_text)
    
    display(ReportText('Exemplary text'*100))
    
    #will not work in some projects, restrict usage 
    display(Markdown('Formatted text'*100)) 
    
    
## CELL 3
## Math 

    #!!! BE SURE ALL PREVIOUS CELLS ARE RUN !!!#
    #!!!       BECAUSE OF NEEDED IMPORTS    !!!#

    from sympy import Eq, Symbol, symbols
    
    sec_formula = Section('Section that presents formulas reporting')
    CurrentContainer(sec_formula)
    
    display(ReportText('Mathematical formulas are reported with the support of sympy and it\\'s symbols.'))
    
    a,b = symbols('a b')
    display(SympyFormula(Eq(a,b)))


## CELL 4
## Picture
    
    #!!! BE SURE ALL PREVIOUS CELLS ARE RUN !!!#
    #!!!       BECAUSE OF NEEDED IMPORTS    !!!#
    
    sec_picture = Section('Section that presents pictures reporting')
    CurrentContainer(sec_picture)

    display(Picture('./dynpy/models/images/taipei101.png',caption = 'Caption of picture'))



## CELL 5
## Document

    #!!! BE SURE ALL PREVIOUS CELLS ARE RUN !!!#
    #!!!       BECAUSE OF NEEDED IMPORTS    !!!#

    # Creating file
    # Be sure *output* folder is in the current directory

    guide_name = './output/report_name' #path for report file 

    doc = Guide(guide_name)
    doc.append(sec_text) # adding certain sections
    doc.append(sec_formula)
    doc.append(sec_picture)
    # Generating file
    doc.generate_pdf(clean_tex=True)
    


"""

)
        
        display(IPMarkdown(preliminary_str))    

        
        preliminary_str=(
"""
#Perform basic setup for document creation.

#This method initializes the document and prepares it for content addition.

#Example:

#To prepare a simple document with text and images:

#Good practice here is to allocate 1 section per 1 cell

## ############### CELL 1 ###########################
## Imports

from dynpy.utilities.report import *
from dynpy.utilities.templates.document import Guide

doc = Guide('./output/report_name')
    

## ############### CELL 2 ###########################
## Text reporting
    
sec_text = Section('Section that presents text reporting')
CurrentContainer(sec_text)

display(ReportText('Exemplary text'*100))

#will not work in some projects, restrict usage 
display(Markdown('Formatted text'*100)) 
    
    
## ############### CELL 3 ###########################
## Math 

from sympy import Eq, Symbol, symbols

sec_formula = Section('Section that presents formulas reporting')
CurrentContainer(sec_formula)

display(ReportText('Mathematical formulas are reported with the support of sympy and it\\'s symbols.'))

a,b = symbols('a b')
display(SympyFormula(Eq(a,b)))

## ############### CELL 4 ###########################
## Picture

sec_picture = Section('Section that presents pictures reporting')
CurrentContainer(sec_picture)

display(Picture('./dynpy/models/images/taipei101.png',caption = 'Caption of picture'))



## ############### CELL 5 ###########################
## Document

# Creating file
# Be sure *output* folder is in the current directory

guide_name = './output/report_name' #path for report file 

doc = Guide(guide_name)
doc.append(sec_text) # adding certain sections
doc.append(sec_formula)
doc.append(sec_picture)
# Generating file
doc.generate_pdf(clean_tex=True)

""")    
        return ObjectCode(preliminary_str) 
    
    
    
    @property
    def _report_components(self):
        
        comp_list=[
        mech_comp.TitlePageComponent,
        # mech_comp.SchemeComponent,
        # mech_comp.ExemplaryPictureComponent,
        # mech_comp.KineticEnergyComponent,
        # mech_comp.PotentialEnergyComponent,
        # mech_comp.LagrangianComponent,
        # mech_comp.GoverningEquationComponent,
        # #mech_comp.FundamentalMatrixComponent,
        # mech_comp.GeneralSolutionComponent,
        # #mech_comp.SteadySolutionComponent,
   
        ]
        
        return comp_list
    
    @property
    def default_reported_object(self):
        
        return None

    @property
    def reported_object(self):

        reported_obj=self._reported_object
        
        if reported_obj is None:
            return self.default_reported_object
        else:
            return reported_obj
        

    @reported_object.setter
    def reported_object(self,value):

        self._reported_object=value


    def append_components(self,reported_object=None):

        #self.reported_object = reported_object
        
        doc=self

        for comp in self._report_components:
            doc.append(comp(self.reported_object))

        return None
    

        
class Guide(Document, ReportMethods):
    """
        A class to generate a structured LaTeX document with pre-configured packages and settings.

        Inherits from `Document` and provides additional methods to simplify LaTeX report creation.

        Attributes:
            _documentclass (str): The LaTeX document class (default is 'article').
            latex_name (str): Name of the document.
            packages (List[Union[Package, Command]]): List of LaTeX packages and commands to include in the document.
            _reported_object (Optional[object]): The object being reported on, if any.

        Exemplary Usage:
            >>> from dynpy.utilities.report import *
            >>> from dynpy.utilities.documents.guides import Guide

            >>> doc = Guide('./output/sample_report', title="Sample Report")

            >>> section = Section('Exemplary section name')
            >>> CurrentContainer(section)

            >>> display(Markdown(''' Exemplary Markdown text in the section '''))
            >>> display(ReportText(' Exemplary text appended into section '))

            >>> doc.append(section)

            >>> doc.generate_pdf(clean_tex=True)



        Example of Customization of the document properties:
            >>> from dynpy.utilities.report import *
            >>> from dynpy.utilities.documents.guides import Guide

            >>> custom_geometry = ['lmargin=20mm', 'rmargin=20mm', 'top=25mm', 'bmargin=25mm']

            >>> doc = Guide(
            >>>     default_filepath='./output/custom_report',
            >>>     title='Custom Report',
            >>>     geometry_options=custom_geometry
            >>> )

            >>> section = Section('Exemplary Custom Section Name')

            >>> doc.append(section)

            >>> doc.generate_pdf(clean_tex=True)
    """

    _documentclass = 'article'
    latex_name = 'document'
    packages = [
                  Package('geometry',options=['lmargin=25mm', 'rmargin=25mm',  'top=30mm', 'bmargin=25mm', 'headheight=50mm']),
                  Package('microtype'),
                  Package('authoraftertitle'),
                  Package('polski',options=['MeX']),
                  #Package('geometry',options=['lmargin=25mm', 'rmargin=25mm',  'top=30mm', 'bmargin=25mm', 'headheight=50mm']),
                  Package('listings'),
                  Package('titlesec'),
                  Package('fancyhdr'),
                  Command('pagestyle', arguments=['fancy']),
                  Command('fancyhf', arguments=['']),
                  Command('fancyhead',  arguments=['DynPy Team'],options=['R']),
                  Command('fancyhead', arguments=['Mechanical vibration, 2023'],options=['L']),
                  Command('fancyfoot', arguments=[NoEscape('\\thepage')],options=['C']),
                  ]

    def __init__(
            self,
            default_filepath: str = 'default_filepath',
            title: str = 'Basic title',
            reported_object: Optional[object] = None,
            *,
            documentclass: Optional[str] = None,
            document_options: Optional[List[str]] = None,
            fontenc: str = 'T1',
            inputenc: str = 'utf8',
            font_size: str = 'normalsize',
            lmodern: bool = False,
            textcomp: bool = True,
            microtype: bool = True,
            page_numbers: bool = True,
            indent: Optional[Union[str, int]] = None,
            geometry_options: Optional[List[str]] = None,
            data: Optional[dict] = None,
    ):
        """
            Initialize the Guide class with optional customization.

            Args:
                default_filepath (str): Path for the generated document.
                title (str): Title of the document.
                reported_object (Optional[object]): Object being reported on, if any.
                documentclass (Optional[str]): LaTeX document class (e.g., 'article').
                document_options (Optional[List[str]]): Options for the document class.
                fontenc (str): Font encoding (default 'T1').
                inputenc (str): Input encoding (default 'utf8').
                font_size (str): Font size (default 'normalsize').
                lmodern (bool): Whether to use Latin Modern fonts.
                textcomp (bool): Whether to use the `textcomp` package.
                microtype (bool): Whether to use the `microtype` package.
                page_numbers (bool): Whether to include page numbers.
                indent (Optional[Union[str, int]]): Indentation settings.
                geometry_options (Optional[List[str]]): Geometry options for page layout.
                data (Optional[dict]): Additional data for customization.
        """

        if documentclass is not None: self._documentclass

        self._reported_object = reported_object
        
        super().__init__(
            default_filepath=default_filepath,
            documentclass=self._documentclass,
            document_options=document_options,
            fontenc=fontenc,
            inputenc=inputenc,
            font_size=font_size,
            lmodern=lmodern,
            textcomp=textcomp,
            microtype=microtype,
            page_numbers=page_numbers,
            indent=indent,
            geometry_options=geometry_options,
            data=data,
        )

#         label=self.label
        self.title='Mechanical vibration'
        #self.packages.append(Command('title', arguments=[NoEscape(self.title)]))
        #self.packages.append(Command('author', arguments=['DynPy Team']))
        self.packages.append(Command('date', arguments=[NoEscape('\\today')]))
        #self.append(Command('maketitle'))
        self.append(NewPage())
        # tu implementować co tam potrzeba
        self.append_components()


class ExampleTemplate(Guide):
    pass



class EngeneeringDrawingGuide(Guide):
    
    latex_name = 'document'
    packages = [
                  Package('geometry',options=['lmargin=25mm', 'rmargin=25mm',  'top=30mm', 'bmargin=25mm', 'headheight=50mm']),
                  Package('microtype'),
                  Package('authoraftertitle'),
                  Package('polski',options=['MeX']),
                  #Package('geometry',options=['lmargin=25mm', 'rmargin=25mm',  'top=30mm', 'bmargin=25mm', 'headheight=50mm']),
                  Package('listings'),
                  Package('titlesec'),
                  Package('fancyhdr'),
                  Command('pagestyle', arguments=['fancy']),
                  Command('fancyhf', arguments=['']),
                  Command('fancyhead',  arguments=['DynPy Team'],options=['R']),
                  Command('fancyhead', arguments=['Engeneering Drawing, 2023'],options=['L']),
                  Command('fancyfoot', arguments=[NoEscape('\\thepage')],options=['C']),
    ]
    
    
class DevelopmentGuide(Guide):
    
    latex_name = 'document'
    packages = [
                  Package('geometry',options=['lmargin=25mm', 'rmargin=25mm',  'top=30mm', 'bmargin=25mm', 'headheight=50mm']),
                  Package('microtype'),
                  Package('authoraftertitle'),
                  Package('polski',options=['MeX']),
                  #Package('geometry',options=['lmargin=25mm', 'rmargin=25mm',  'top=30mm', 'bmargin=25mm', 'headheight=50mm']),
                  Package('listings'),
                  Package('titlesec'),
                  Package('fancyhdr'),
                  Command('pagestyle', arguments=['fancy']),
                  Command('fancyhf', arguments=['']),
                  Command('fancyhead',  arguments=['DynPy Team'],options=['R']),
                  Command('fancyhead', arguments=['DynPy development guide, 2023'],options=['L']),
                  Command('fancyfoot', arguments=[NoEscape('\\thepage')],options=['C']),
        ]

        
        
class IntroToCocalcGuideV2(Guide):

    @property
    def _report_components(self):
        
        comp_list=[

#             github_comp.CocalcLoginComponent,
#              development_comp.JupyterSetUpComponent,
#             github_comp.CocalcFolderComponent,

#             github_comp.CocalcDynSysListComponent,
            reporting_comp.ReportingBasicsComponent,

        ]

        return comp_list
        
        
class IntroToCocalcGuide(Guide):

    @property
    def _report_components(self):
        
        comp_list=[

            #github_comp.CocalcLoginComponent,
            github_comp.CocalcUsageComponent,
            development_comp.JupyterSetUpComponent,
            github_comp.CocalcFolderComponent,

            github_comp.CocalcDynSysListComponent,
            reporting_comp.ReportingBasicsComponent,
            

        ]

        return comp_list

class UsageOfDynamicSystemsGuide(Guide):

    @property
    def _report_components(self):

        comp_list=[
            systems_comp.DynamicSystemsUsageIntroComponent,
            systems_comp.DynamicSystemCallComponent,
            systems_comp.DynamicSystemMethodsUsageComponent,

            pandas_comp.NumericalAnalysisSimulationComponent,
            
            systems_comp.SimulationsComponent, # entire component to rewrite
            reporting_comp.SimulationReportComponent,

        ]

        return comp_list
    
    @property
    def default_reported_object(self):
        
        #from ...models.mechanics.tmac import SDOFWinchSystem
        from ...models.mechanics import ForcedSpringMassSystem as DynamicSystem
        
        return DynamicSystem()

class IntroToPandasGuide(Guide):

    @property
    def _report_components(self):

        comp_list=[
            pandas_comp.IntroToPandasUsageComponent,
            pandas_comp.PandasTableGenerationComponent,
            pandas_comp.PandasMethodsComponent,
            reporting_comp.BasicOperationsComponent,
            systems_comp.DynamicSystemCallComponent,
            systems_comp.SimulationsComponent, #Common with *UsageOfDynamicSystemsGuide* class
            reporting_comp.DifferentSimulationsComponent,


        ]

        return comp_list

    @property
    def default_reported_object(self):

        #from ...models.mechanics.tmac import SDOFWinchSystem
        from ...models.mechanics import ForcedSpringMassSystem as DynamicSystem

        return DynamicSystem()
    
    
    
class BasicsOfODESystemGuide(Guide):

    @property
    def _report_components(self):

        comp_list=[
            systems_comp.ODESystemsUsageIntroComponent,
            reporting_comp.BasicUsageOfODESystemComponent,
            #reporting_comp.ODEReportComponent,
            reporting_comp.ReportCompUseComponent,
            reporting_comp.ProjectileExampleComponent,
            systems_comp.ODESimulationComponent,
            systems_comp.ODENumericalSimulationsComponent

        ]

        return comp_list



class BasicsOfDynSysImplementationGuide(UsageOfDynamicSystemsGuide):

    @property
    def _report_components(self):

        comp_list=[
            systems_comp.BasicsOfDynSysImplementationIntroComponent,
            systems_comp.DynSysImplementationComponent,
            systems_comp.DynamicSystemCallComponent,
            systems_comp.DynamicSystemMethodsUsageComponent,
            systems_comp.SimulationsComponent,
            systems_comp.DynSysCodeComponent,

        ]

        return comp_list


class BasicsOfReportingGuide(UsageOfDynamicSystemsGuide):

    @property
    def _report_components(self):

        comp_list=[
            reporting_comp.BasicsOfReportingIntroComponent,
            reporting_comp.ReportingBasicsComponent,
            systems_comp.DynamicSystemCallComponent,
            systems_comp.SimulationsComponent,
            reporting_comp.SimulationReportComponent,
            reporting_comp.ReportingModuleIntroComponent,
            reporting_comp.LibrariesImportComponent,
            reporting_comp.DocumentComponent,
            reporting_comp.CurrentContainerComponent,
            reporting_comp.ReportTextComponent,
#             guide_comp.
            reporting_comp.PictureComponent,
            reporting_comp.SympyFormulaComponent,
            reporting_comp.DocumentGenerationComponent,
            reporting_comp.PredefinedSectionComponent,
#             guide_comp.
            pandas_comp.TablesCreationComponent,
            reporting_comp.AutomarkerIntroComponent,
            reporting_comp.CodeEmbeddingComponent,

            reporting_comp.UnitRegistryIntroComponent,
            reporting_comp.ReportFormattingGuidelinesComponent,
#             guide_comp.

        ]

        return comp_list

   
class ResearchProjectGuidelines(BasicsOfReportingGuide):

    @property
    def _report_components(self):

        comp_list=[


           development_comp.InterimTemplateComponent,
           development_comp.ModellingInPythonGuidelinesComponent,
            # systems_comp.DynamicSystemCallComponent,
            #systems_comp.SimulationsComponent,
            #reporting_comp.SimulationReportComponent,

        ]

        return comp_list 
    
class ThesisGuidelines(ResearchProjectGuidelines):

    @property
    def _report_components(self):

        comp_list=[


           development_comp.InterimTemplateComponent,
           development_comp.ModellingInPythonGuidelinesComponent,
            # systems_comp.DynamicSystemCallComponent,
            #systems_comp.SimulationsComponent,
            #reporting_comp.SimulationReportComponent,

        ]

        return comp_list


    
    
class InterimProjectGuidelines(ResearchProjectGuidelines):

    @property
    def _report_components(self):

        comp_list=[

            development_comp.InterimScheduleComponent,
            development_comp.InterimTemplateComponent,
#             systems_comp.DynamicSystemCallComponent,
#             systems_comp.SimulationsComponent,
#             reporting_comp.SimulationReportComponent,

        ]

        return comp_list
    
    @property
    def default_reported_object(self):

        #from ...models.mechanics.tmac import SDOFWinchSystem
        #from ...models.odes.linear import LinearFirstOrder
        
        return datetime.datetime(2024,7,13)
    
    

    
class IntroDynPyProjectGuidelines(UsageOfDynamicSystemsGuide):

    @property
    def _report_components(self):

        comp_list=[

            development_comp.PythonBasicsGuidelinesComponent,
            development_comp.InterimTemplateComponent,
#             guide_comp.DynamicSystemCallComponent,
#             guide_comp.SimulationsComponent,
#             guide_comp.SimulationReportComponent,

        ]

        return comp_list
    
    
class BasicsOfReportComponentImplementationGuide(UsageOfDynamicSystemsGuide):

    @property
    def _report_components(self):

        comp_list=[

            reporting_comp.ReportCompImplementationComponent,
            reporting_comp.ReportingCompsUsageComponent,
#             reporting_comp.ReportCompImplementationIssueComponent, #Obecnie jest problem z argumentem reported_object, dokładniej classname i sypie błędem
            reporting_comp.ReportingComponentsList

        ]

        return comp_list
    
    @property
    def default_reported_object(self):

        return None
    
class GithubSynchroGuide(UsageOfDynamicSystemsGuide):

    @property
    def _report_components(self):

        comp_list=[
            github_comp.GithubSynchroIntroComponent,
            github_comp.GitSynchroPanelAccessComponent,
            github_comp.GitSynchroIntroComponent,
            github_comp.UsageOfGitHubInterfacesComponent,
            github_comp.UsageOfMeetingCreatorComponent,
            #github_comp.GithubIssueReportComponent, #komponent do listowania issue, chyba nie jest tutaj potrzebny do pokazania

        ]

        return comp_list
    
    @property
    def default_reported_object(self):

        default_data = {'classname':'GitSynchroPanelAccessComponent',
                       'module':'guide.en.py',
                       'field':'guide or report',
                       'target':'`ODESystem` class',
                       'issue_no':123,
                       }


        return default_data
