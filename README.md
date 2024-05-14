# Python Order Management System

 - **1.** [Introduction](#intro) 
 - **2.** [Context Diagram](#context) 
 - **3.** [User Stories](#stories) 
 - **4.** [Project Plan](#plan) 
 -  **5.** [System Class Diagram](#sys_diagram)
	 - 5.1 [Classes in the OMS](#oms_classes) 
	 - 5.2  [Conceptual Class Diagram of the OMS](#oms_conceptual)
	 - 5.3 	[Bottom-up approach to development](#oms_bottomup)
 -   **6.** [Object-Orientation in OMS](#oms_object)
 -  **7.** [Input Validation in the User Interface class](#input_val)
 -  **8.** [Formatted Output](#format_o)
 -  **9.** [Data Dictionary](#data_dict)
 -  **10.** [File Handling](#file_hand)
 -  **11.** [Pseudocode](#pseudo)
 -  **12.** [Sorting and Searching](#s_and_s)
 -  **13.** [Messaging (modelling dynamic behaviour) in an Object-Oriented system](#messaging)
 	-  13.1 [Polymorphism in the OSM](#polymorph)
 -  **14** [Code optimisation techniques for better collaboration and maintenance](#optimisation)
 	-  14.1 [Intrinsic and Extrinsic documentation](#docs)
  	-  14.2 [Organisation of source code files and modules](#src_org)
 -  **15** [Testing and Quality Assurance](#test_quality)
   	-  15.1 [Black box testing of OMS](#black_box)
 		-  15.1.1 [Test Cases](#test_cases)
		-  15.1.2 [Input-Output table for testing](#io_table)
	- 15.2 [White box testing of OMS](#white_box)
   
## Rubric + Mark Distribution
You must design, implement, debug, test and document an Object-Oriented System. The implementation must be done in Python. You are required to work in groups of three students. If any student does not have a group, your teacher will assign the student to a group of his choice. You are required to submit both the source code and an MS Word documentation file. The minimum requirements of the system and its documentation are:
<ol>
<li>	An introduction to the system: This must also include the challenges and a hint of how you would solve them. (3 marks)</li>
<li>	A high-level context diagram: This must identify the external entities and the input and output interactions between the system and the external entities. (2 marks)</li>
<li>	A list of user stories. (3 marks)</li>
<li>	A project management plan: This should include time in terms of weeks and tasks to be accomplished each week. It should also include who is responsible for each task. (3 marks)</li>
<li>	A UML class diagram of the system must include client-facing classes (namely UI classes) and application logic classes. The application logic classes must be separate from the UI classes. You may either use GUI or textual UI. The class diagram should only include the class's attributes and the method signatures. The data types of the attributes and the parameters should be specified. (10 marks)></li>
<li>	At least one level of OO inheritance in the project: Identify parent-child class relationships wherever possible. The relationships should be visible in the class diagram. (4 marks)</li>
<li>	All user interface classes should have input data validation logic. Ensure runtime exceptions are handled graciously. Meaningful feedback should be provided to the user, especially in case of input errors or run-time errors. (10 marks)</li>
<li>	All output generated by the system should be formatted so that it is easy to read with liberal use of white spaces to group related information. (5 marks)</li>
<li>	A data dictionary table for all attributes in each application logic class. This table should contain the desired columns for data type/data structure, validation, example, description, etc. (10 marks)</li>
<li>	File handling logic: Your code should be able to store, retrieve and update the data in a file. The file format should also be provided in the documentation. (10 marks)</li>
<li>	The pseudocode or flowchart of at least three complex methods in the application logic component or the file handling component. (7 marks)</li>
<li>	Sorting logic: Your code should use at least one of the following sorting algorithms: bubble, selection, insertion, merge.  (3 marks)</li>
<li>	Specify how you handled message-passing between objects. This is usually done using Sequence Diagrams in UML, but your syllabus is silent, so you may describe it in a textual manner. At least one example of an abstract method or one instance of polymorphic behaviour should be included in the project. (7 marks)</li>
<li>	You must document how the source code files are organised using modules and provide documentation for most phases of the Software Development Life Cycle. This may also include documentation on how to install your program from GitHub. Ensure your code has no absolute addressing (path) issues so it can be installed without changing any code. (4 marks)</li>
<li>	Each user story should have a test data table and an Input Output (IO) table. The test data table should include data for testing: valid input, invalid input, and boundary values. The IO table should consist of rows of data in the test data table, and each row entry should have a column for test data and a column for expected output. Unit tests should be conducted to verify that the actual output is the same as the expected output. If not, the logic should be fixed. (10 marks)</li>
<li>	You should use a version control system like GitHub to share the code and the documentation with your teammates and teachers. (1 marks)</li>
<li>	The complete source code should be added as an appendix to the documentation. The source code should have intrinsic documentation. This involves using meaningful variable/method names and documentation of the APIs of each method (specify what it does, the parameters (if any) and its type and the return value (if any). (3 marks)</li>
<li>	Your project should be syntax-free, logical error-free and run-time error-free. This must be demonstrated on an ongoing basis and at least one day before the last date of submission. (5 marks)</li>
</ol>
<b>Note: A partial documentation of a partially completed project for an Order Management System is provided below. Your team may extend this project or develop a new project of your choice with the same level of complexity. In any case, each team should seek the teacher’s approval for the type of extension you want to add before proceeding with your project. You may adapt the documentation given here instead of writing everything from scratch.**</b>

## 1. Introduction<a name="intro"></a>
Order management systems are frequently used in most e-commerce businesses. Some of the challenges of such systems are relating an order with a customer, identifying items in an order, deleting an item before an order is finalised, creating one of more types of order (e.g. regular order, postal order), updating an order, searching for an order in a list of orders, sorting an order, tracking the status of an order, storing and retrieving orders from a file, etc. In this project, a simple order management system will be designed and developed using Python as the implementation language. The project will be created from a user interface perspective, business logic perspective and file handling perspective. Hence, the project comprises three components: UI Component, Application Logic Component and File-Handling Component. This separation of concerns will help better maintain the delivered project since, in the real world, an end user’s interface can be from various devices or platforms. However, the back-end application logic service is delivered via a common platform. Similarly, file handling services can differ due to the many database systems, such as MySQL and Oracle. In this project, database systems will not be used since they are out of the scope of the syllabus. Instead, file handling will be used. An overview of the architecture is shown in Figure 1.

![Picture1](https://github.com/sebastian-power/order-management-system/assets/52031320/4471a6ab-bc9a-4604-b8c6-094140ca4ddd)
<i>Figure 1: Overview of the architecture</i>

An IS project has to follow the Software Development Life Cycle (SDLC) phases. This project starts with the requirements phase of the SDLC, where an overview of the external actors and their interactions with the system is first identified using a context diagram (section 2). This is followed by the definition of user stories (section 3). In the planning phase of the SDLC, a project plan is drawn to estimate the effort required in terms of time and roles for the development team (section 4). In the analysis phase of the SDLC, abstraction principles are used to identify likely classes in the OMS (section 5). As part of the SDLC’s design phase, the details of how the inheritance principle in OOP is applied in this project are discussed in section 6. A discussion on how input data is validated is considered in section 7. The output generated by the system needs to be formatted. This is discussed in section 8. The data type and structure of the attributes in each class are considered in the discussion of the data dictionary (section 9). The design of file-handling algorithms is considered in section 10. The design of complex algorithms in the application logic component is considered in sections 11 (pseudocode) and 12 (sorting and searching). The modelling of the system's dynamic behaviour is considered in section 13. 

## 2. Context Diagram<a name="context"></a>
The interactions between the end user and the order management system can be depicted via a context diagram, as shown below in Figure 2. Further details of the context diagram are not shown to keep this document brief wherever possible.

![image](https://github.com/sebastian-power/order-management-system/assets/52031320/ef87dcf8-fb60-491c-8f48-564e14088033)

<i>Figure 2: Context Diagram</i>

## 3. User Stories<a name="stories"></a>
User Stories are typically used in Agile frameworks to articulate how each software feature will add value to the user. Each user story is the smallest unit of work in an agile framework and has the following structure:
“As a [person], I [want to], [so that].”  
An incomplete set of user stories for the OMS are provided below. <i>Note: Your actual report should have a complete list of user stories</i>:
<ol>
	<li>As an IT literate Customer, I want to create an Order using my PC so that I can save time travelling to the shop</li>
	<li>As an aged customer, I want to create a Postal Order so that the order can be delivered to my address.</li>
	<li>As a Postal Order customer, I want to track the status of my order so that I can be sure it is delivered at home.</li>
	<li>As a recurring customer, I want to be able to search for an Order from previous histories so that I can submit my expenses to my accountant at any time.</li>
	<li>As a Sales Officer, I want to create an order on behalf of my customer so that I can keep my customers happy.</li>
	<li>As a customer, I need to get a sorted report based on the order dates of all my previous orders so that I can view them offline.</li>
	<li>As a customer, I want to change the details of an order before its submission so that I can manage my budget better.</li>
</ol>

## 4. Project Plan<a name="plan"></a>
The project is planned to be completed in 5 weeks. Observe that the project plan includes planning, analysis, design, implementation and testing tasks from the Software Development Life Cycle (SDLC). It also includes details such as how much of the work is accomplished and the roles of each team member. Note: Please remind me to upload an editable version of this plan on Google Classroom.
Project Management plan here(fake gantt chart)
<i>Figure 3: Project Management Plan</i>
## 5. System Class Diagram<a name="sys_diagram"></a>
### 5.1 Classes in the OMS<a name="oms_classes"></a>
Figure 5 shows the set of classes used in the OMS from a conceptual perspective. The classes are colour-coded to be consistent with the components used in the architecture diagram in Figure 1. In addition, in Figure 5, <<keyword>> notation is used to represent the classifier of the classes. {class} or {interface} could be used as a namespace for various classifiers. A classifier comprises Unified Modelling Language (UML) elements with standard features. In Figure 5, a <<boundary>> class is used to represent it deals with user interaction features but has no application logic for managing a business activity. On the other hand, the <<datatype>> classes only deal with file-handling operations and are used by the application logic components. Once the data from a file is read or written, the information is passed to the <<entity>> or <<actor>> classes, which represent the application logic of the business.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/b9d9b89c-fdec-441b-a0ee-2f604ed587e0)
<i>Figure 5: Conceptual perspective of the Classes used in OMS</i>
Finer details of the features in each class are specified in Figure 6 (from a specification perspective). I have yet to include the classes for file handling here, but you need to include such classes in the report, too. Most details of each class are self-explanatory. However, special attention must be given to the Postal_Order class since it is inherited from the Order class. That is, all the attributes and methods of the Order are available in the Postal_Order class by default. Hence, these are shown in lighter-coloured text in Figure 6. In addition, it also has its own attributes, such as current_status, o_delivery_date and o_past_states. A Postal_Order differs from an Order by its state being able to be tracked, and the delivery date is one month from the order date. On the other hand, it is assumed that an Order will not be delivered. Hence, the above attributes should be included in the Postal_Order class. So, since a Postal_Order is a particular type of Order, it is designed as an inherited Order class.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/fbae7398-eeb3-4ac9-a50e-947310843ea0)
<i>Figure 6: Class details from a specification’s perspective</i>
### 5.2 Conceptual Class Diagram of the OMS<a name="oms_conceptual"></a>
A class diagram depicts a static nature of how the various classes are associated with one another in the system. In UML, an association is a relationship between classes. For example, it can be used to show that instances of classes could be linked to each other or combined logically or physically into some aggregation. Figure 7 depicts the class diagram of the OMS. 
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/1e074def-e5a1-49d7-8dbc-14180c85ea5e)
<i>Figure 7: Class Diagram of the OMS</i>
An aggregation represents a whole-part association. The whole (aggregator) contains parts (aggregates). A diamond shape at the whole end denotes aggregation. For example, in OMS, the Order_Mgt_UI class has an aggregation of Order and Postal Order. A stronger form of aggregation is a composition. Here, the parts are tightly bound to the whole and are denoted by a black-filled diamond shape at the whole end. For example, An Order should have a customer and at least one Order_Item, and If an Order is deleted, the corresponding Customer and Order_Item details will also be deleted. Such an association is composition. Additional information such as arity and navigability are sometimes also specified in class diagrams. Arity refers to how many class instances can be associated with the other class. Navigability identifies the direction of the association. Let’s first consider arity in Figure 7. An Order_Mgt_UI class can exist with 0 or more Order(s) or with 0 or more Post_Order(s). This is represented by 0..n in the diagram, and the arrow of the association indicates the direction. For example, the direction of the association arrow is from the Order_Mgt_UI to the Postal_Oder to suggest that the Order_Mgt_UI class has the Postal_Order and not the other way around. An X mark is sometimes indicated on the association line to explicitly tell that a particular direction of association is not possible. For example, Figure 7 depicts a Postal_Order class object that is not navigable from a Postal_Order_DB class object.
### 5.3 Bottom-up approach to development<a name="oms_bottomup"></a>
This project uses several classes. The complexity of the design and development of projects with many classes in OOP can be reduced using either a bottom-up or a top-down approach. A bottom-up approach is considered for the OMS because bottom-up is more amenable to incremental development. In incremental development, independent classes are developed, tested, and debugged first, and then the dependent classes are developed, tested, and debugged before integrating them to build a concrete solution.  So, the bottom-up approach allows for early detection of errors, leading to smoother integration. Order_Mgt_UI is an example of a top-level class in the OMS project since it uses other classes. Another example of a top-level class is the Order class since it is dependent on Oder_DB, Order_Item and Customer classes. On the other hand, Order_DB is a bottom-level class.
## 6. Object-Orientation in OMS<a name="oms_object"></a>
Object-oriented programming is popular because it enables the evaluation of existing classes without changing them. This reduces the maintenance cost. For example, a new inherited class can be created if a new attribute is required for a previously existing class. In Figure 7, inheritance is depicted. A triangular arrow is drawn from the Postal_Order class to the Order class for the inheritance reasons explained in section 5.1.
## 7. Input Validation in the User Interface<a name="input_val"></a>
Validating user input on the client side saves valuable maintenance time. This section explains how validation is incorporated when an Order_Item is ordered in an Order. A snippet of the code is provided in Figure 8, and the corresponding runtime interactive output statement is shown in Figure 9. Observe that a list of available products is first displayed, and then a choice is presented to the user to select an item number rather than asking the user to enter the item's name, which is more error-prone. In addition, the code checks for negative values and runtime errors if the user wrongly inputs non-numeric values for the item quantity. Similarly, input validation is performed for other inputs but is not illustrated here for space brevity. Please see the code in the appendix for complete details.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/b7638213-699d-4880-8032-6eee66245e91)
<i>Figure 8: Code snippet for validation during input of an Order_Item</i>
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/5c426f10-4452-43e8-8574-3883e09e1445)
<i>Figure 9: Runtime example of input validation for Order_Item</i>
## 8. Formatted Output<a name="format_o"></a>
A snip of the formatted output provided by the program is shown in Figure 10. 
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/4c7b2ffa-4b9f-4d11-b62a-7dd5aa695718)
<i>Figure 10: Formatted Output</i>
The output clearly illustrates how the Postal Order details are grouped separately and how white space is used for readability.
## 9. Data Dictionary<a name="data_dict"></a>
A data dictionary comprehensively describes each attribute and class variable used in the system. Note that it is not all variables. Data dictionaries are valuable during the system's post-delivery maintenance. A data dictionary commonly includes variable name, data type, format, size in bytes, and the number of characters to display the item, including the number of decimal places (if applicable), the purpose of the variable, and a relevant example. Any validation rules applicable to the data item can also be included. Details of records or arrays of records should be included in data dictionaries. In this report, a data dictionary is shown in Figure 11_1 and Figure 11_2, describing all the attributes of only the Order class. However, your report must contain a table for all attributes in each class in the project.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/11fa6feb-7b85-4625-9150-b1cd42e9dd38)
<i>Figure 11_1: Data Dictionary of the attributes in the Order class</i>
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/8f55fca4-0b02-415a-92a5-de562901cc58)
<i>Figure 11_2: Data Dictionary of the attributes in the Order class</i>
An example of how a customer variable will be displayed in string form:
Customer details are:
Customer ID =Cust_2024_1         Customer name =Chris               Customer email =Chris@c.com  
An example of how the items variable will be displayed in string form:
	Item name = Pen                                     Item price =$2.00      Item Qty = 3
## 10. File Handling<a name="file_hand"></a>
File handling classes such as Customer_DB, Order_DB, Customer_DB, Order_Item_DB and Products_DB contain the logic for storing, retrieving, and updating the corresponding data in files. Navigation of these classes is always from the corresponding entity.
## 11. Pseudocode<a name="pseudo"></a>
Pseudocode is usually used to illustrate the design of complex system parts. A complex part of a Postal_Order class is the algorithm to find whether a postal order has transitioned through all the states before it is delivered to the customer. This section contains the high-level pseudocode of the has_partial_valid_state_sequence method in the Postal Order class.  The algorithm assumes the valid states of  Postal Order are "Initiated", "Packed", "Shipped", and "Delivered". A postal order can transition from “Initiated” to “Packed” to “Shipped” and then to a “Delivered” state. Please assume that the algorithm needs to keep track of the current and past states as it transitions from one state to another. We can use a variable, states, to hold the list of past states of a Postal_Order. The has_partial_valid_state_sequence method can be used before updating the list of states. From this discussion, it is evident that the list of valid values in the list states can be one of the following: [ ] or  [“Initiated”] or [“Initiated”, “Packed”] or [“Initiated”, “Packed”, “Shipped] or [“Initiated”, “Packed”, “Shipped, “Delivered”]. The algorithm is as follows:
```
#states is the param containing the past states of a Postal Order. This can be any one of the lists mentioned above in blue text.
#valid_sequence is the param containing the list of valid states: [“Initiated”, “Packed”, “Shipped, “Delivered”]
function has_partial_valid_state_sequence(states, valid_sequence):
        IF the length of states > length of valid_sequence THEN
            RETURN “not valid”
        ENDIF
        FOR index = 0 to (length of states) -1
             IF states[index] is not equal to the first item in valid_sequence THEN
                  RETURN not valid
		    ELSE 
				Remove the first item in valid_sequence so that the following item now becomes the first
             ENDIF
        NEXT index
        RETURN “valid” 
END
```
Similarly, you must identify all other complex algorithms in each class and write their pseudocode in this section.
## 12. Sorting and Searching<a name="s_and_s"></a>
Sorting and searching are some of the ubiquitous operations in Information Systems. They are frequently used in order management systems to search for a product among thousands of products, sort the items in an order based on the price or the product's name, etc. Several types of searching and sorting algorithms are used in information systems, and each type's efficiency varies. The HSC exams typically contain questions on sorting and searching. However, this document does not contain any scoring algorithms. Please add a sorting algorithm in the Order class to sort all orders based on each item's product name or price. Alternatively, add a sorting algorithm in a new class that manages all orders. Since the sorting algorithms are standard, you must illustrate that you can adapt them for a specific purpose.
## 13. Messaging (modelling dynamic behaviour) in an Object-Oriented system<a name="messaging"></a>
Class diagrams do not depict what methods and classes come into play from among the classes and methods in the system. for a specific purpose, such as a user story. For example, a software maintenance engineer may be interested in fixing a feature related to a user story. In such a case, a model such as a class diagram containing all the details of an OO system reduces the maintenance engineer's productivity. Hence, separate models for each user story are essential. In this section, the system's dynamic behaviour for user story 3.2 (As an aged customer, I want to create a Postal Order so that the order can be delivered to my address.) in section 3 is considered. A sequence diagram is usually used to model this, but the HSC syllabus needs to mention it. So, instead, a textual approach will be used to explain how messages are passed from one object to another when a user story needs to be satisfied. In OOP, message passing is a fundamental concept that enables objects to communicate with each other within a program.
The following invocations of methods from various classes are needed to get a Postal_Order object:
An end user starts interacting with the OMS through the Order_Mgt_UI object. Let order_mgt_ui be a reference to the Order_Mgt_UI object.
The definition of the constructor of this class is provided below:
```
    def __init__(self):
        self.cust_name=self.get_cust_name()
        self.cust_email=self.get_cust_email()
        #testing below: Creation of a regular Order and a Postal Order
        self.orders=[self.create_postal_order()]
```
Observe that the constructor of the object makes calls to get_cust_name(),  get_cust_email() and create_postal_order() methods to initialise its attributes cust_name, cust_email and orders, respectively. These attributes can be seen in the abstract definition of the Order_Mgt_UI class in Figure 6. The class diagram in Figure 6 is principally used to find the attributes and method signatures of all classes in the system. The method signatures of get_cust_name() and get_cust_email()  in Figure 6 indicate they return a string each, representing a customer name and email from the keyboard. 
The get_create_postal_order(): Postal_Order method signature in the Order_Mgt_UI class can create a Postal_Order. 
The sequence of messages so far is as follows:
```
     order_mgt_ui
     |
         |->get_cust_name()
         |->get_cust_email()
         |->create_postal_order()
```
The definition of create_postal_order() provides more information about the sequence of messaging:
```
    def create_postal_order(self):
        a_customer = Customer(self.cust_name,self.cust_email)
        a_postal_order = Postal_Order(a_customer)
        done=False
        while not done:
            done=True
            a_postal_order.add_item(self.create_order_item())
            correct_more=False
            while not correct_more:
                correct_more=True
                more = input("Do you want to order another item Y/N: ")
                more = more.strip()
                if more not in ['Y', 'y','N','n']:
                     print("You did not enter Y or N. Please try again")
                     correct_more=False
            if more in ['Y','y']:
                 done=False
        return a_postal_order
```
It first calls the constructor of the Customer class by passing cust_name and cust_email as arguments, which in turn calls the setter methods in the Customer class by default.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/0e5dfa3c-effb-4b5b-8a44-4a8d30b1de61)
It then invokes the constructor of Postal_Order. The constructor of the Postal_Order class is shown below.
```
    def __init__(self, customer:Customer):
        super().__init__(customer)
        one_month_from_now=(datetime.now()+timedelta(days=30))#one month from now
        self.o_delivery_date=one_month_from_now       
        self.past_states=[] 
        self.current_state=0#current state is, "initiated", among past states
```
Since Postal_Order inherits from Order, it first calls the constructor of the Order class, where the setter methods of the Order class attributes are called by default.
```
    def __init__(self, customer:Customer):
        Order.order_num +=1
        self.order_id=str(Order.order_num)
        self.customer = customer
        self.order_date= datetime.now()
        self.items = []  # Initialize an empty list to store order items
```
<br></br>
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/5dd51e34-ec4c-48e2-ae02-8987cc2d904b)

At this stage, the user interface class has a Postal_Order object but no order items in the Postal_Object. That is why the Postal Order’s add_item() method is invoked in the outer while loop of the create_postal_order() method in the Order_mgt_UI class to add one or more Order_Item objects. The inherited add_item() method of the Postal_Order class requires an Order_Item object as an argument. Hence, it invokes the create_order_item() method of the user interface class to get the details of an Order_Item from the keyboard before invoking the add_item() method. The create_order_item() also uses the Product class to get the name and price of each item, but this has not been shown in the following messaging structure due to lack of space.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/de2bc2ca-4213-45b7-a412-7eb0ec08d390)
In summary, each object in an OOP project is a self-contained unit with its data and behaviour (methods), and an object is not the same as a class. A class is a template (like a cookie cutter) that consists of data members or variables and functions and defines the attributes and methods for potential objects to be created in the future. An object is an instance of a class(like a cookie created using the cookie cutter), and each object has its values for the different attributes present in its class. This feature allows multiple developers to work on other parts of the program simultaneously, as they can create their classes and objects. When an object (the sender) needs to communicate with another object (the receiver), it sends a message. The receiver processes the message, performs the requested action, or provides the requested data. This communication is essential for building modular, reusable, and maintainable software systems. 
### 13.1 Polymorphism in the OSM<a name="polymorph"></a>
Polymorphism in OOP refers to exhibiting different behaviours by inherited methods with the same signature depending on the associated object. In the OSM, the Postal_Order class inherits from the Order class. The Order class is the parent class, and the Postal_Order class is the child class. Additionally, only the str() method has the same signature. When the str() method is called on an Order object, it returns the string representation instance attributes of the Order object. In contrast, when the same str() method is called on a Postal_Order object, it returns the string representation of the Postal_Order attributes. This is shown below.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/38bfbbcd-2083-4e26-90a3-aa2151adc8d8)
The above table shows the difference between the two methods regarding additional information, such as the delivery date and the states in the postal order’s str() method. 
## 14. Code optimisation techniques for better collaboration and maintenance<a name="optimisation"></a>
Most Information System projects are created in groups. An essential component of collaboration within object-oriented programming is the ability for developers to understand how each other operates. This can be done in several ways. One approach is providing Intrinsic and extrinsic documentation during the SDLC phases. Another way is by providing a consistent directory structure for each team member’s source code. These two approaches are considered below.
### 14.1 Intrinsic and extrinsic documentation<a name="docs"></a>
Intrinsic documentation exists within the code and directly relates to its readability and understanding. It facilitates collaboration among team members by providing context and guidance. Examples of intrinsic documentation include (i) Using meaningful names for variables, classes, functions and code directories. (ii) Adding comments in the code to provide explanations, clarify intent, or guide other programmers. (iii) Consistent naming conventions for variable, function, and class names enhance code readability. (iv) Inline documentation in the form of brief explanations within the code for method signatures and parameter descriptions. A cursory glance at the source code in the appendix indicates these conventions have been followed. An example is given below:
```
    #Returns true if the 'states' parameter has a set of valid states. Returns False otherwise
    #Parameter ‘valid_sequence’ has values ["Initiated", "Packed", "Shipped", "Delivered"]
    #A Postal order's valid partial state sequence can only have the following form:
    #[]
    #["initiated"],
    #["Initiated", "Packed"]
    #["Initiated", "Packed", "Shipped"],
    #["Initiated", "Packed", "Shipped", "Delivered"]
    def has_partial_valid_state_sequence(self,states:type[list[int]], valid_sequence:list[type[str]])->type[bool]:
```
### 14.2 Organization of source code files and modules<a name="src_org"></a>
Organising the project files and assets into appropriate directories is crucial for maintaining a clean and efficient codebase. The directory structure of the OMS project is as follows:
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/0aa6008a-46c0-40a9-8413-f13bb97bfdf3)
Note that some of the directories are empty, but the available structure makes it easy to locate where, for example, a Products_DB.py or a products.txt file should be placed.
Note: Python can throw ModuleNotFoundError or an import error if the import statements are not correctly specified when the source file(s) need to import another module (s). A module is a Python file only when another file imports it. Moreover, a module may use relative import or absolute import. The advantages of relative imports are conciseness and the ability to rearrange the paths of large packages without editing the paths to the sub-packages. However, relative imports are only sometimes as readable as absolute ones.  For more information on the difference between relative and absolute imports, read Absolute and Relative Imports in Python - GeeksforGeeks.
The import statements in the various files for the given directory structure in the OMS project are provided in the above directory structure to illustrate how the relative and absolute imports were used.  
## 15. Testing and Quality Assurance<a name="test_quality"></a>
In software engineering, there are different testing levels to ensure a software product's quality. These levels include unit testing, subsystem testing, and system testing. Unit testing focuses on verifying the functionality of each component or module of the software application. Developers typically perform it by testing the components in isolation. Subsystem testing is a type of integration testing that verifies the behaviour and interaction between multiple components or modules within a subsystem. It ensures that the subsystem functions are as expected and meet the specified requirements. System testing checks whether the software, hardware, or product meets the specified requirements. It focuses on validating the entire system's functionality and is usually done by developers and testers.
The tests mentioned above are usually conducted using a black-box testing approach. Black box testing is performed when the inputs and expected outputs are known. These tests assert whether the expected output for a series of instructions or test data matches the actual output. Despite conducting these tests correctly, if the assertion fails, then white-box testing is performed. White box testing is a technique requiring explicit knowledge of the internal workings of the code being tested. Though programmers can conduct it while testing for syntax, logic, or runtime errors, it is only used to check for logic or runtime errors after performing the black box testing. An example could be a developer testing whether the attributes of an object were changed correctly or whether a function modified the value in a variable correctly.
### 15.1 Black box testing of OMS<a name="black_box"></a>
Black box unit tests of some of the classes in OMS were performed using the Visual Studio Code (VSC) IDE’s pytest framework. Details of how to configure VSC for unit tests are available at Testing Python in Visual Studio Code. This section illustrates how the Postal_Order’s has_partial_valid_state_sequence(self,states:type[list[int]], valid_sequence:list[type[str]])->type[bool] method can be unit tested. This is our test case.
### 15.1.1 Test Cases<a name="test_cases"></a>
A test case is a sequence of actions to verify a specific functionality. It outlines the necessary steps, prerequisites, inputs and expected outcomes for testing a particular functionality. The pre-requisite for testing the case is that a Postal_Order  and a Customer object must be available.
### 15.1.2 Input-Output table for testing<a name="io_table"></a>
From the earlier discussion on its intrinsic documentation in section 14.1, we know the list of valid states of a Postal_Order object. An Input-Output (IO) table is provided to document a list of valid and invalid inputs for the states of a Postal_Order.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/7f7448cf-e1cd-456c-9298-d2effd0ecf8e)
The test data in the IO table can be used to create a test suite for has_partial_valid_state_sequence. A test suite was developed based on the IO table entries. This is shown in the figure below.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/a512ceca-ffb5-4ac2-829c-d47c53bd2a7f)
Observe that all the test cases in the IO tables are tested. 
### 15.2 White box testing of OMS<a name="white_box"></a>
The code passed all the test cases except test case number 10. White box testing and debugging using breakpoints and line-by-line tracing was used to identify a logical error in Postal_Order.  Consequently, statement numbers 61 to 63 were added to fix the error.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/f3f84bc1-6b0f-41fc-8529-c4ef7d4075cc)
The output of VSC following the bug fix is shown below:
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/0e9e237d-008e-4635-b88d-9841bf82eb49)
