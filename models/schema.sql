-- Employees Table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    JobTitle VARCHAR(100),
    DepartmentID INT,
    RoleID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID),
    FOREIGN KEY (RoleID) REFERENCES Roles(RoleID)
);

-- Departments Table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100),
    Description TEXT,
    DepartmentHead INT,
    FOREIGN KEY (DepartmentHead) REFERENCES Employees(EmployeeID)
);

-- Roles Table
CREATE TABLE Roles (
    RoleID INT PRIMARY KEY,
    RoleName VARCHAR(100),
    Description TEXT
);

-- AuditTrail Table
CREATE TABLE AuditTrail (
    AuditTrailID INT PRIMARY KEY,
    EmployeeID INT,
    ActionType VARCHAR(50),
    Timestamp TIMESTAMP,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Attendance Table
CREATE TABLE Attendance (
    AttendanceID INT PRIMARY KEY,
    EmployeeID INT,
    ClockInTime DATETIME,
    ClockOutTime DATETIME,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- AccessControlLogs Table
CREATE TABLE AccessControlLogs (
    LogID INT PRIMARY KEY,
    EmployeeID INT,
    ActionType VARCHAR(50),
    Timestamp TIMESTAMP,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- LeaveRequests Table
CREATE TABLE LeaveRequests (
    RequestID  VARCHAR(50) PRIMARY KEY,
    EmployeeID VARCHAR(50),
    LeaveType VARCHAR(100),
    StartDate DATE,
    EndDate DATE,
    Status VARCHAR(50),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- UserRoles Table
CREATE TABLE UserRoles (
    UserID INT,
    RoleID INT,
    PRIMARY KEY (UserID, RoleID),
    FOREIGN KEY (UserID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (RoleID) REFERENCES Roles(RoleID)
);

-- PerformanceGoals Table
CREATE TABLE PerformanceGoals (
    GoalID INT PRIMARY KEY,
    EmployeeID INT,
    GoalDescription TEXT,
    Deadline DATE,
    Status VARCHAR(50),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- TrainingPrograms Table
CREATE TABLE TrainingPrograms (
    ProgramID INT PRIMARY KEY,
    ProgramName VARCHAR(100),
    Trainer VARCHAR(100),
    Schedule VARCHAR(100),
    Description TEXT
);

-- CommunicationLogs Table
CREATE TABLE CommunicationLogs (
    LogID INT PRIMARY KEY,
    SenderID INT,
    ReceiverID INT,
    MessageType VARCHAR(50),
    MessageContent TEXT,
    Timestamp TIMESTAMP,
    FOREIGN KEY (SenderID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (ReceiverID) REFERENCES Employees(EmployeeID)
);

-- ChatbotLogs Table
CREATE TABLE ChatbotLogs (
    LogID INT PRIMARY KEY,
    UserID INT,
    Query TEXT,
    Response TEXT,
    Timestamp TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Employees(EmployeeID)
);

-- DoorAccessEvents Table
CREATE TABLE DoorAccessEvents (
    EventID INT PRIMARY KEY,
    EmployeeID INT,
    EventType VARCHAR(50),
    Timestamp TIMESTAMP,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- BenefitPrograms Table
CREATE TABLE BenefitPrograms (
    ProgramID INT PRIMARY KEY,
    ProgramName VARCHAR(100),
    Description TEXT
);

-- BenefitSelections Table
CREATE TABLE BenefitSelections (
    SelectionID INT PRIMARY KEY,
    EmployeeID INT,
    ProgramID INT,
    SelectionDetails TEXT,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (ProgramID) REFERENCES BenefitPrograms(ProgramID)
);

-- PayrollDetails Table
CREATE TABLE PayrollDetails (
    PayrollID INT PRIMARY KEY,
    EmployeeID INT,
    Month INT,
    Year INT,
    SalaryDetails DECIMAL(10, 2),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);