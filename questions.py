# questions.py
import random

# Complete Master Exam Database (Exactly 100 Questions calibrated to match the sample test definitions)
RAW_QUESTION_BANK = [
    # === UNIT 1: AGGREGATE PLANNING OPTIMISATION (11 Questions) ===
    {
        "unit": "Unit 1 - Aggregate Planning Optimisation",
        "question": "Which of the following best describes what Aggregate Planning specifies?",
        "options": [
            "The procurement plan for raw materials across suppliers",
            "The exact production schedule for each individual SKU per day",
            "The production of product family units and the necessary production capacities by resource type for each planning period"
        ],
        "correct": 2
    },
    {
        "unit": "Unit 1 - Aggregate Planning Optimisation",
        "question": "What is the primary planning horizon for Aggregate Production Planning (APP)?",
        "options": [
            "Short-term hourly and daily scheduling adjustments",
            "Medium-term operational matching of demand and supply, typically from 3 to 18 months",
            "Long-term macro strategic decisions spanning 5 to 10 years"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 1 - Aggregate Planning Optimisation",
        "question": "Which modeling framework is standard for incorporating inventory levels, workforce modifications, backorders, and capacity limits simultaneously?",
        "options": [
            "Mixed-Integer Linear Programming (MILP)",
            "Simple Moving Average regression metrics",
            "First-Come, First-Served priority rules"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 1 - Aggregate Planning Optimisation",
        "question": "In a corporate Aggregate Planning MILP model, an inventory balance constraint dictates that:",
        "options": [
            "Ending Inventory = Beginning Inventory + Production - Demand",
            "Ending Inventory = Demand - Capacity + Backorders",
            "Ending Inventory = Beginning Inventory - Firing + Hiring"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 1 - Aggregate Planning Optimisation",
        "question": "A pure 'chase strategy' in aggregate planning centers on:",
        "options": [
            "Maintaining constant production lines and absorbing deviations using inventory buffers",
            "Adjusting capacity and workforce levels dynamically to follow fluctuating demand patterns closely",
            "Subcontracting the entirety of corporate operations to external firms"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 1 - Aggregate Planning Optimisation",
        "question": "A pure 'level strategy' in aggregate production planning is characterized by:",
        "options": [
            "Varying human resource levels daily to match changing incoming orders",
            "Maintaining a steady production output rate and workforce size, using inventory/backorders to absorb demand fluctuations",
            "Modifying machine setup metrics dynamically inside single workstations"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 1 - Aggregate Planning Optimisation",
        "question": "Which mathematical direction is applied to the objective function when solving standard APP problems?",
        "options": [
            "Maximization of raw warehouse capacity thresholds",
            "Minimization of total system operational costs (production, inventory, labor adjustments, backorders)",
            "Minimization of the total product variants offered"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 1 - Aggregate Planning Optimisation",
        "question": "Which of the following would be classified as an operational input parameter (constant) rather than a decision variable in an APP model?",
        "options": [
            "Demand forecasts, machine capacities, and specific labor cost rules",
            "The total volume of products to manufacture during period t",
            "The exact number of temporary operators to hire at the start of period t"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 1 - Aggregate Planning Optimisation",
        "question": "What is a main limitation of using continuous linear programming without integer elements for aggregate planning?",
        "options": [
            "It cannot determine minimum cost alternatives",
            "It struggles to represent discrete entities like fractional human operators or binary hiring/firing policies accurately",
            "It is computationally too heavy for modern solver architectures"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 1 - Aggregate Planning Optimisation",
        "question": "What does a backordering variable represent in an aggregate planning constraint?",
        "options": [
            "Fulfilling demand in a period later than it was requested, usually incurring a penalty cost",
            "Pre-purchasing component materials before demand forecasts are processed",
            "Selling idle production capacity to external manufacturing partners"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 1 - Aggregate Planning Optimisation",
        "question": "Which software utility framework is recommended in the MUCEIM slides to model and solve the aggregate planning MILP equations?",
        "options": [
            "Excel Goal Seek menus exclusively",
            "Pyomo mathematical modeling language in Python",
            "Simulink block diagrams in MATLAB"
        ],
        "correct": 1
    },

    # === UNIT 2: MATERIALS REQUIREMENT PLANNING OPTIMISATION (11 Questions) ===
    {
        "unit": "Unit 2 - Materials Requirement Planning Optimisation",
        "question": "What does Material Requirements Planning specify and schedule?",
        "options": [
            "Net requirements for components and materials, along with their production or purchase in each planning period",
            "Long-term financial budgets and annual staffing plans for departments",
            "Machine maintenance intervals without considering material quantities"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 2 - Materials Requirement Planning Optimisation",
        "question": "Which primary input structural graph details the exact parent-component relationships and quantities needed for assembly?",
        "options": [
            "The Precedence Matrix Graph",
            "The Bill of Materials (BOM)",
            "The Taillard Routing Instance Sheet"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 2 - Materials Requirement Planning Optimisation",
        "question": "In standard MRP calculations, Net Requirements are equal to:",
        "options": [
            "Gross Requirements - Scheduled Receipts - Available Inventory from the previous period",
            "Gross Requirements + Ordering Costs + Warehouse Storage Costs",
            "Planned Order Releases multiplied by Lead Time Offset variances"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 2 - Materials Requirement Planning Optimisation",
        "question": "What does 'Lead Time Offset' mean within an MRP system calculation?",
        "options": [
            "Pushing planned order completions out into future planning periods",
            "Determining Planned Order Releases by shifting Planned Order Receipts backward in time based on component lead times",
            "Multiplying on-hand stock indexes by manufacturing setup values"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 2 - Materials Requirement Planning Optimisation",
        "question": "Which lot-sizing heuristic balances setup and holding costs step-by-step by selecting lots that minimize the cost per unit?",
        "options": [
            "Lot-for-Lot (L4L)",
            "Minimum Unit Cost (MUC)",
            "Silver-Meal Sequence Bound"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 2 - Materials Requirement Planning Optimisation",
        "question": "What does the lot-sizing abbreviation 'MTC' refer to in material planning systems?",
        "options": [
            "Minimum Total Cost",
            "Maximum Time Capacity",
            "Multi-Threaded Calculation"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 2 - Materials Requirement Planning Optimisation",
        "question": "The abbreviation 'SMM' stands for which standard material lotification technique?",
        "options": [
            "Stochastic Machine Mapping",
            "Silver-Meal Method",
            "Single Model Manufacturing"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 2 - Materials Requirement Planning Optimisation",
        "question": "What is a defining operational trait of a 'Lot-for-Lot' (L4L) planning policy?",
        "options": [
            "It aggregates an entire year's forecast into a single large production batch",
            "It sets planned order quantities exactly equal to the net requirements of each separate period",
            "It maintains a fixed, unchangeable safety inventory of 100 units at all times"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 2 - Materials Requirement Planning Optimisation",
        "question": "What does the term 'MRP Explosion' refer to?",
        "options": [
            "A catastrophic failure of automated hardware assets during runtime operations",
            "The calculation process that determines lower-level component gross requirements based on parent planned order releases",
            "An execution error caused by conflicting constraint ranges in Pyomo solvers"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 2 - Materials Requirement Planning Optimisation",
        "question": "If a manager adjusts Order Costs or Holding Costs within an MRP test dataset, what will change?",
        "options": [
            "It alters the optimal grouping of periods under cost heuristics like MUC, MTC, or SMM",
            "It breaks the structural parent-child links defined inside the master BOM graph",
            "It causes standard linear programming relaxations to become mathematically infeasible"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 2 - Materials Requirement Planning Optimisation",
        "question": "What is meant by 'Scheduled Receipts' within time-phased MRP records?",
        "options": [
            "Open orders that have already been released and are committed to arrive at the start of a specific period",
            "Un-factored consumer demand estimates pulled from macro forecasting models",
            "The planned future batches that have not yet been approved or sent to suppliers"
        ],
        "correct": 0
    },

    # === UNIT 3: ECONOMIC LOT SCHEDULING OPTIMISATION (11 Questions) ===
    {
        "unit": "Unit 3 - Economic Lot Scheduling Optimisation",
        "question": "In the ELSP, what is the fundamental challenge that production managers face when multiple products share a single production line?",
        "options": [
            "Balancing setup costs, inventory costs, and backlog costs to minimise total operational costs",
            "Maximising production rates for each individual product",
            "Determining which product generates the highest revenue"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 3 - Economic Lot Scheduling Optimisation",
        "question": "Which heuristic algorithm selects the next item to produce based on which product will exhaust its inventory stock first?",
        "options": [
            "Monden's Method",
            "Run-Out Method",
            "Johnson's Sequence Rule"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 3 - Economic Lot Scheduling Optimisation",
        "question": "What logical issue occurs in a basic Run-Out Method implementation if the same product is scheduled twice consecutively?",
        "options": [
            "The optimization loop crashes immediately due to a division by zero error",
            "An unnecessary setup time/cost is counted, even though the machine is already configured for that product",
            "The total calculated schedule length becomes infinite"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 3 - Economic Lot Scheduling Optimisation",
        "question": "When optimizing the ELSP with a Genetic Algorithm, what serves as a more effective stopping condition than a fixed iteration loop counter?",
        "options": [
            "Stopping as soon as total warehouse stock equals raw demand",
            "Monitoring population fitness trends and stopping when convergence shows no meaningful improvement over several consecutive generations",
            "Aborting the program immediately when an invalid sequence string is generated"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 3 - Economic Lot Scheduling Optimisation",
        "question": "Which performance metrics are typically plotted to analyze population convergence in an ELSP Genetic Algorithm simulation?",
        "options": [
            "Minimum, average, and maximum fitness values across generations",
            "Individual operation processing times across workstations",
            "Workforce hiring and firing trends over planning horizons"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 3 - Economic Lot Scheduling Optimisation",
        "question": "What parameters define the baseline problem structure of the ELSP?",
        "options": [
            "Product demand rates, production rates, setup costs, and inventory holding values",
            "Precedence diagrams, workstation task counts, and idle metrics",
            "Workforce limits, hiring variables, and macro warehouse capacity boundaries"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 3 - Economic Lot Scheduling Optimisation",
        "question": "Why is the ELSP structurally more complex than the traditional single-item Economic Order Quantity (EOQ) model?",
        "options": [
            "Multiple distinct products compete for production time on a single, shared manufacturing resource without overlapping",
            "It uses continuous variables without any configuration setup considerations",
            "It is restricted to manual mathematical optimization procedures"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 3 - Economic Lot Scheduling Optimisation",
        "question": "What is the operational definition of 'Run-Out Time' for a product in a warehouse?",
        "options": [
            "The time required to change a machine configuration over to a new tool setup",
            "The estimated time until current on-hand inventory is completely depleted based on average demand consumption rates",
            "The processing lead time of a sub-component listed inside the master BOM structure"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 3 - Economic Lot Scheduling Optimisation",
        "question": "In a Genetic Algorithm context, what does 'chromosomal representation' refer to?",
        "options": [
            "The specific data structure encoding a candidate production sequence solution within the population",
            "The physical floor plan of an automated assembly layout",
            "The capital budget required to procure raw materials"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 3 - Economic Lot Scheduling Optimisation",
        "question": "What is the function of a fitness function inside an ELSP Genetic Algorithm setup?",
        "options": [
            "It tracks the physical speed of operators handling tool changeovers",
            "It measures the overall cost performance of a candidate sequence to guide evolutionary selection",
            "It counts the total lines of code within the optimization scripts"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 3 - Economic Lot Scheduling Optimisation",
        "question": "What defines 'feasibility' in the context of the ELSP?",
        "options": [
            "Finding a production schedule that satisfies demand for all items over time without stockouts or overlapping runs on the shared asset",
            "Ensuring that the total number of components matches parent BOM requirements exactly",
            "Ensuring that the line balancing efficiency reaches 100%"
        ],
        "correct": 0
    },

    # === UNIT 4: FLOW SHOP SCHEDULING OPTIMISATION (11 Questions) ===
    {
        "unit": "Unit 4 - Flow Shop Scheduling Optimisation",
        "question": "What does 'unit machine capacity' mean in the context of Flow Shop Scheduling?",
        "options": [
            "Each machine can process an unlimited number of jobs simultaneously",
            "Each machine is assigned to exactly one job type",
            "No machine can perform more than one operation at a time"
        ],
        "correct": 2
    },
    {
        "unit": "Unit 4 - Flow Shop Scheduling Optimisation",
        "question": "What is the defining layout characteristic of a standard Flow Shop production line?",
        "options": [
            "Jobs follow variable routing paths through different manufacturing departments",
            "All jobs must pass through all available machines in the exact same sequence order",
            "Resources move continuously around a stationary product assembly"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 4 - Flow Shop Scheduling Optimisation",
        "question": "Which algorithm provides an exact optimal sequence for a 2-machine Flow Shop problem to minimize makespan ($C_{max}$)?",
        "options": [
            "Monden's Heuristic",
            "Johnson's Algorithm",
            "The Hungarian Assignment Method"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 4 - Flow Shop Scheduling Optimisation",
        "question": "How can Johnson's Algorithm principles be applied to approximate M-machine Flow Shop problems?",
        "options": [
            "By grouping physical assets into fictitious surrogate machine pairs to generate sequencing heuristics based on aggregate processing times",
            "By transforming the entire routing structure into a single unconstrained linear equation",
            "By applying the Hungarian matrix reduction technique to assign tasks to specific resources"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 4 - Flow Shop Scheduling Optimisation",
        "question": "Which exact Branch & Bound solution strategy systematically searches a state tree to find guaranteed optimal flow shop schedules?",
        "options": [
            "Lomnicki's Method",
            "The Hungarian Matrix Assignment Rules",
            "The Run-Out Time Search Heuristic"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 4 - Flow Shop Scheduling Optimisation",
        "question": "What outcome often occurs during Johnson's generalized algorithm when processing time ties happen?",
        "options": [
            "The solver script encounters a division error and halts immediately",
            "Multiple alternative optimal or near-optimal job sequences emerge from the choice framework",
            "The instance converts directly into an ordinary job shop configuration"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 4 - Flow Shop Scheduling Optimisation",
        "question": "What primary objective metric is typically minimized in classic Flow Shop optimization models?",
        "options": [
            "Total operator hiring variances across consecutive periods",
            "The makespan ($C_{max}$), representing the total completion time of the entire set of jobs",
            "The total number of assembly levels documented in the BOM"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 4 - Flow Shop Scheduling Optimisation",
        "question": "What is a major trade-off between Lomnicki's exact Branch & Bound method and heuristic setups like Johnson's approximations for large problems?",
        "options": [
            "Lomnicki's method guarantees absolute optimality but faces exponential computational growth, whereas heuristics solve quickly but cannot guarantee optimality",
            "Heuristics require significantly more processing memory than exact tree search routines",
            "Lomnicki's tree search can only run if machine processing times are zero"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 4 - Flow Shop Scheduling Optimisation",
        "question": "In Flow Shop context, what defines a 'Permutation Flow Shop'?",
        "options": [
            "A layout where the processing order of jobs can change arbitrarily at each machine",
            "A subset of flow shops where every single machine processes the set of jobs in the exact same sequence order",
            "A scheduling matrix solved exclusively through Hungarian row-reduction steps"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 4 - Flow Shop Scheduling Optimisation",
        "question": "What is the primary role of calculating lower bounds in Lomnicki's Branch & Bound algorithm?",
        "options": [
            "To estimate the best possible makespan for a partial sequence, allowing unpromising search branches to be pruned early",
            "To define the average lot sizing grouping for an MRP explosion loop",
            "To adjust workforce levels dynamically between consecutive planning periods"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 4 - Flow Shop Scheduling Optimisation",
        "question": "Which visual chart displays the timeline of job sequences moving across successive machines?",
        "options": [
            "Gantt Chart",
            "Precedence Diagram Network",
            "BOM Hierarchical Tree"
        ],
        "correct": 0
    },

    # === UNIT 5: JOB SHOP SCHEDULING OPTIMISATION (12 Questions) ===
    {
        "unit": "Unit 5 - Job Shop Scheduling Optimisation",
        "question": "What is the main objective of the Job Shop Scheduling Problem?",
        "options": [
            "To minimise the total makespan while respecting precedence constraints and machine capacity",
            "To maximise the number of jobs processed per machine",
            "To balance the workload equally across all machines"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 5 - Job Shop Scheduling Optimisation",
        "question": "What differentiates a Job Shop scheduling problem from a standard Flow Shop scheduling problem?",
        "options": [
            "Job Shop routing is uniform across all items",
            "Each individual job has a customized and independent machine routing path with varying operation times",
            "Job Shops do not include setup or processing time dependencies"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 5 - Job Shop Scheduling Optimisation",
        "question": "What does the abbreviation 'PDR' stand for in shop-floor operational scheduling terminology?",
        "options": [
            "Priority Dispatching Rules",
            "Parametric Digital Routing",
            "Product Demand Ratio"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 5 - Job Shop Scheduling Optimisation",
        "question": "Which of the following is a common heuristic Priority Dispatching Rule (PDR) used on shop floors?",
        "options": [
            "Monden's sequence spacing rule",
            "Shortest Processing Time (SPT)",
            "The Hungarian Matrix Assignment algorithm"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 5 - Job Shop Scheduling Optimisation",
        "question": "Which local search metaheuristic uses memory structures called 'Tabu lists' to escape local optima in job shops?",
        "options": [
            "Genetic Algorithms",
            "Tabu Search (TS)",
            "Branch & Bound tree search"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 5 - Job Shop Scheduling Optimisation",
        "question": "What famous benchmark sets are used in the course assignments to test PDR and Tabu Search algorithm scripts?",
        "options": [
            "Monden automotive profiles",
            "Taillard's benchmark instances (specifically the 8taxx9 sets)",
            "Silver-Meal lotization profiles"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 5 - Job Shop Scheduling Optimisation",
        "question": "What is the primary role of the 'Tabu List' mechanism within local search metaheuristics?",
        "options": [
            "To record the best global objective values achieved during execution",
            "To temporarily forbid recently executed search moves, preventing the algorithm from cycling in local optima",
            "To screen out structurally infeasible job combinations before execution begins"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 5 - Job Shop Scheduling Optimisation",
        "question": "What metric represents the benchmark target often extracted from the 'UB' column of Taillard instance solutions?",
        "options": [
            "The Upper Bound value of the optimal makespan ($C_{max}$)",
            "The total operational warehouse storage cost index",
            "The line balance efficiency score"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 5 - Job Shop Scheduling Optimisation",
        "question": "What is a major operational limitation of using simple Priority Dispatching Rules (PDR) for complex job shops?",
        "options": [
            "They are too computationally heavy to run on modern computers",
            "They are greedy and short-sighted, frequently resulting in schedules far from the global mathematical optimum",
            "They cannot handle jobs requiring more than two processing operations"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 5 - Job Shop Scheduling Optimisation",
        "question": "What does the 'Earliest Due Date' (EDD) dispatching rule prioritize?",
        "options": [
            "The job with the shortest processing time on the current active machine",
            "The job with the closest, most immediate delivery deadline",
            "The job that unlocks the largest number of downstream operations"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 5 - Job Shop Scheduling Optimisation",
        "question": "What happens when a Tabu Search algorithm encounters a solution that satisfies an 'aspiration criterion'?",
        "options": [
            "The solution is accepted even if it is currently on the tabu list, typically because it improves upon the best solution found so far",
            "The algorithm halts immediately and logs an execution failure",
            "The tabu list memory is completely wiped"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 5 - Job Shop Scheduling Optimisation",
        "question": "What is the role of a 'converter' when working with Taillard instances for a Job Shop scheduling project?",
        "options": [
            "To parse and translate the instance text file into matrices of machine order sequences and operation processing times for your code",
            "To automatically convert continuous variables into binary integers",
            "To compute line balance efficiency scores"
        ],
        "correct": 0
    },

    # === UNIT 6: JOB-RESOURCE ASSIGNMENT OPTIMISATION (11 Questions) ===
    {
        "unit": "Unit 6 - Job-Resource Assignment Optimisation",
        "question": "Which feature is associated with the ordinary assignment problem?",
        "options": [
            "One-to-one matching between N jobs and N resources",
            "Resources can process multiple jobs subject to capacity constraints",
            "NP-hard complexity for all ordinary instances"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 6 - Job-Resource Assignment Optimisation",
        "question": "What classical, exact polynomial-time algorithm solves the Ordinary Assignment Problem optimally with $O(n^3)$ computational complexity?",
        "options": [
            "Lomnicki's Branch & Bound Method",
            "The Hungarian Method",
            "The Run-Out Method Heuristic"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 6 - Job-Resource Assignment Optimisation",
        "question": "What decision variable type is utilized to formulate an Ordinary Job-Resource Assignment model in a Mixed-Integer Linear Program?",
        "options": [
            "Continuous non-negative decision parameters",
            "Binary decision variables ($x_{ij} \in \{0, 1\}$)",
            "Unconstrained continuous values"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 6 - Job-Resource Assignment Optimisation",
        "question": "The structural constraints of an Ordinary Assignment mathematical model enforce that:",
        "options": [
            "Each job is assigned to exactly one resource, and each resource is assigned to exactly one job",
            "The total cycle time of assignments cannot exceed the available workstation count",
            "The total output must equal the time-phased component gross requirements"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 6 - Job-Resource Assignment Optimisation",
        "question": "What differentiates a Generalised Assignment Problem from an Ordinary Assignment Problem?",
        "options": [
            "The Generalised Assignment variant removes capacity constraints entirely",
            "Resources have specific capacity limitations allowing them to accept multiple job assignments simultaneously",
            "It can only be resolved using manual matrix calculation rules"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 6 - Job-Resource Assignment Optimisation",
        "question": "What constitutes the objective function configuration for a standard Job-Resource Assignment model?",
        "options": [
            "Minimizing the total sum of assignment costs or processing times across all chosen matches",
            "Maximizing the idle variances between separate factory sectors",
            "Minimizing the number of distinct components documented inside an active BOM sheet"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 6 - Job-Resource Assignment Optimisation",
        "question": "What core matrix operations are executed when performing manual reduction loops within the Hungarian Method?",
        "options": [
            "Row and column cost subtractions to identify an optimal set of zero-cost assignments",
            "Multiplying job processing speeds by workforce hiring adjustment costs",
            "Adding parent safety margins to component net requirements tables"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 6 - Job-Resource Assignment Optimisation",
        "question": "If a cost matrix is not square (jobs do not equal resources) in an ordinary assignment problem, how is it pre-processed?",
        "options": [
            "The problem is flagged as mathematically infeasible and aborted",
            "Dummy rows or columns with zero or highly penalized costs are introduced to balance the matrix dimensions",
            "The smallest jobs are combined until the matrix balances"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 6 - Job-Resource Assignment Optimisation",
        "question": "In an ordinary assignment constraint $\sum_{j} x_{ij} = 1$, what does this mathematically ensure for each job $i$?",
        "options": [
            "That job $i$ is assigned to exactly one resource",
            "That resource $j$ can accept multiple parallel operations",
            "That the cost of the assignment remains equal to 1"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 6 - Job-Resource Assignment Optimisation",
        "question": "Why can the ordinary assignment problem be solved efficiently using its linear programming relaxation without needing explicit integer branch steps?",
        "options": [
            "The problem possesses a totally unimodular constraint matrix structure, which guarantees integer solutions",
            "The problem is highly non-linear and bypasses linear programming bounds",
            "The model relies entirely on randomized local search metaheuristics"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 6 - Job-Resource Assignment Optimisation",
        "question": "What does a cost matrix entry of infinity ($\infty$) signify in an assignment problem?",
        "options": [
            "A forbidden assignment link that the optimization model cannot choose",
            "A zero-cost dummy link that balances the matrix dimensions",
            "An assignment that maximizes line balancing efficiency scores"
        ],
        "correct": 0
    },

    # === UNIT 7: MIXED-MODEL SEQUENCING OPTIMISATION (11 Questions) ===
    {
        "unit": "Unit 7 - Mixed-Model Sequencing Optimisation",
        "question": "What is the fundamental challenge in Mixed-Model Sequencing Problems?",
        "options": [
            "Determining the optimal number of workers per station",
            "Determining the optimal sequence of products to minimise disruptions in component consumption rates",
            "Determining the optimal number of product variants to manufacture"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 7 - Mixed-Model Sequencing Optimisation",
        "question": "Which heuristic approach is applied to manage mixed-model sequencing variations within the Toyota Production System framework?",
        "options": [
            "Lomnicki's Branch & Bound tree search",
            "Monden's Method",
            "The Hungarian Matrix Assignment Rule"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 7 - Mixed-Model Sequencing Optimisation",
        "question": "When optimizing mixed models via a Genetic Algorithm, what does Option A for chromosome encoding define?",
        "options": [
            "Genes are coded directly as product identity numbers within the sequence chain",
            "Genes represent sequence position index parameters requiring deep decoding logic",
            "Genes represent workforce capacity hiring variations across multi-period windows"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 7 - Mixed-Model Sequencing Optimisation",
        "question": "What advantage can Option A chromosome encoding offer over sequence position encoding (Option B)?",
        "options": [
            "It increases code complexity and run times",
            "It evaluates chromosome tracking metrics more quickly and provides better results in less computation time",
            "It entirely removes the need to calculate part consumption levels"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 7 - Mixed-Model Sequencing Optimisation",
        "question": "What optional structural parameter can be introduced to model sequencing preferences, such as keeping cars of the same color close together?",
        "options": [
            "Component net requirement offsets",
            "Attraction energy or setup grouping metrics for specific product features",
            "Workforce structural adjustment variance factors"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 7 - Mixed-Model Sequencing Optimisation",
        "question": "What is a core objective of Monden's Method in a mixed-model assembly line setup?",
        "options": [
            "To maximize total warehouse inventory volumes",
            "To smooth the consumption rate of different components over time, keeping it close to constant target levels",
            "To isolate assembly work centers using large inventory buffers"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 7 - Mixed-Model Sequencing Optimisation",
        "question": "What happens if a mixed-model sequence is poorly planned and groups too many high-workload variants consecutively?",
        "options": [
            "The line experiences work overloads, stations exceed cycle time limits, and the assembly line may stall",
            "The total demand volume automatically shrinks to fit line capacities",
            "The instance converts into an ordinary assignment problem profile"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 7 - Mixed-Model Sequencing Optimisation",
        "question": "What input parameters must be provided to evaluate a mixed-model sequencing heuristic?",
        "options": [
            "The list of product variants, their production quantities, and the component requirements per product model",
            "The employee hiring and firing cost matrices across planning horizons",
            "The total downstream task successors listed in a line graph template"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 7 - Mixed-Model Sequencing Optimisation",
        "question": "In a Genetic Algorithm for mixed-model scheduling, what do crossover operations do?",
        "options": [
            "They combine sub-sequences from two parent chromosomes to produce new offspring sequences that inherit their scheduling traits",
            "They mathematically prove that a candidate sequence represents the absolute global minimum cost solution",
            "They delete half of the product variants to speed up optimization runs"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 7 - Mixed-Model Sequencing Optimisation",
        "question": "What occurs during a 'mutation' step in a mixed-model Genetic Algorithm run?",
        "options": [
            "Two random genes within a chromosome sequence are swapped to maintain exploration diversity",
            "The entire population is replaced by copies of the best individual solution",
            "A linear relaxation step is executed to remove integer bounds"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 7 - Mixed-Model Sequencing Optimisation",
        "question": "What type of assembly line configuration is the primary target for Mixed-Model Sequencing models?",
        "options": [
            "A single flexible line where different models or variants of a product are assembled simultaneously without requiring long shutdown setups",
            "A traditional batch line that shuts down for days to swap tooling infrastructure between variants",
            "A line dedicated exclusively to a single uniform standard product model"
        ],
        "correct": 0
    },

    # === UNIT 8: ASSEMBLY LINE BALANCING OPTIMISATION (11 Questions) ===
    {
        "unit": "Unit 8 - Assembly Line Balancing Optimisation",
        "question": "In the ALBP, what does the cycle time constraint define for each workstation?",
        "options": [
            "The minimum number of tasks that must be assigned to it",
            "The exact number of workers required at each station",
            "The maximum capacity (time) available at each workstation"
        ],
        "correct": 2
    },
    {
        "unit": "Unit 8 - Assembly Line Balancing Optimisation",
        "question": "What do precedence constraints represent within an Assembly Line Balancing problem structure?",
        "options": [
            "The financial cost hierarchy of alternative equipment upgrades",
            "The mandatory technological sequencing order requiring certain tasks to be fully completed before downstream tasks can begin",
            "The ratio of permanent workers versus temporary operators"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 8 - Assembly Line Balancing Optimisation",
        "question": "Which heuristic algorithm serves as the classic baseline constructive method for the ALBP by sorting tasks by processing times?",
        "options": [
            "The Run-Out Method",
            "The Largest Candidate Rule (LCR)",
            "Monden's Heuristic Method"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 8 - Assembly Line Balancing Optimisation",
        "question": "What priority rule prioritizes tasks based on the number of downstream successors they unlock in the precedence graph?",
        "options": [
            "The Followers First priority rule",
            "The Shortest Processing Time dispatching rule",
            "The Hungarian matrix allocation rule"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 8 - Assembly Line Balancing Optimisation",
        "question": "How is Line Efficiency ($\eta$) calculated in an Assembly Line Balancing evaluation?",
        "options": [
            "$\eta = \sum t_i / (m \cdot C)$, where $t_i$ are task times, $m$ is the station count, and $C$ is the cycle time",
            "$\eta = \text{Total Production Volume} / \text{Workforce Hiring Cost}$",
            "$\eta = \text{Total Successors} / \text{Total Idle Time}$"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 8 - Assembly Line Balancing Optimisation",
        "question": "What does a constructive heuristic for the ALBP do when an eligible task does not fit within the remaining time of the current workstation?",
        "options": [
            "It closes the current workstation and opens a new workstation to assign the task",
            "It shortens the task's processing time until it fits",
            "It violates the precedence rule to place the task elsewhere"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 8 - Assembly Line Balancing Optimisation",
        "question": "What constitutes Total Idle Time ($I$) across a balanced assembly line?",
        "options": [
            "The sum across all workstations of the cycle time minus the actual total station time ($I = \sum (C - T_s)$)",
            "The time an operator spends executing setup configurations",
            "The total lead time shift recorded inside the parent BOM sheet"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 8 - Assembly Line Balancing Optimisation",
        "question": "What method serves as the exact benchmark to evaluate the solution quality of constructive line heuristics like LCR?",
        "options": [
            "The greedy Run-Out method profile",
            "An exact Mixed-Integer Linear Programming (MILP) model formulation solved to optimality",
            "A manual row-reduction Hungarian matrix template"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 8 - Assembly Line Balancing Optimisation",
        "question": "In the ALBP, what condition defines whether a task is 'eligible' to be assigned to a workstation?",
        "options": [
            "All of its predecessor tasks have already been fully assigned, and its task time fits within the current workstation's remaining time",
            "The task has the longest processing time among all items in the database",
            "The task is listed as a parent component inside the master MRP explosion chart"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 8 - Assembly Line Balancing Optimisation",
        "question": "What is the primary benchmark goal of the Type 1 Assembly Line Balancing Problem (ALBP-1)?",
        "options": [
            "Minimizing the number of workstations required for a fixed, predetermined cycle time",
            "Minimizing the cycle time for a fixed, predetermined number of workstations",
            "Maximizing the sequence-dependent setup costs across a shared machine asset"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 8 - Assembly Line Balancing Optimisation",
        "question": "What is the primary goal of the Type 2 Assembly Line Balancing Problem (ALBP-2)?",
        "options": [
            "Minimizing the cycle time for a fixed, predetermined number of workstations",
            "Minimizing the number of workstations for a fixed cycle time",
            "Maximizing the total sum of assignment costs across a square matrix"
        ],
        "correct": 0
    },

    # === UNIT 9: RESOURCE ALLOCATION OPTIMISATION (11 Questions) ===
    {
        "unit": "Unit 9 - Resource Allocation Optimisation",
        "question": "What is the primary objective of the Resource Allocation Problem?",
        "options": [
            "To complete the project within a specified deadline at the lowest possible cost while satisfying constraints",
            "To maximize the number of tasks executed at the same time regardless of cost",
            "To eliminate all task dependencies before scheduling begins"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 9 - Resource Allocation Optimisation",
        "question": "What distinguishes Resource Allocation Optimisation (Unit 9) from Assembly Line Balancing (Unit 8)?",
        "options": [
            "Unit 8 balances workloads across production workstations, whereas Unit 9 involves the effective deployment of organizational resources (people, skills, budgets) across functions and activities",
            "Unit 9 focuses exclusively on sequence-dependent product setups",
            "Unit 8 is solved by exact solvers, whereas Unit 9 can only be modeled with greedy heuristics"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 9 - Resource Allocation Optimisation",
        "question": "What specific heuristic scheduling method is introduced in Unit 9 to optimize resource deployment?",
        "options": [
            "The Monden Assembly Line Sequencing Method",
            "The Manpower Scheduling Method (MSM)",
            "The Johnson Two-Machine Formulation"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 9 - Resource Allocation Optimisation",
        "question": "What strategy helps ensure an exact MILP model finds a solution for large resource allocation datasets within a reasonable time?",
        "options": [
            "Setting a specific optimality GAP percentage value within the solver parameters",
            "Disabling integer branching steps entirely to run an unconstrained continuous linear relaxation",
            "Forcing the solver to run for a minimum of 24 hours without stopping"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 9 - Resource Allocation Optimisation",
        "question": "What metrics are compared when evaluating the performance of the Manpower Scheduling Method (MSM) against an exact MILP model solution?",
        "options": [
            "Solution optimality (objective value performance) and total computational execution time",
            "The total number of parent levels inside an active BOM diagram",
            "The line efficiency percentage and individual task idle time values"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 9 - Resource Allocation Optimisation",
        "question": "What resources are typically optimized within a Unit 9 Resource Allocation framework?",
        "options": [
            "People, cross-functional skills, project teams, budgets, and technical equipment",
            "Product variants tracking along a single assembly conveyor line",
            "Parent items and component lead times listed in a time-phased spreadsheet"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 9 - Resource Allocation Optimisation",
        "question": "What does an automated 'synthetic data generator' do within a scheduling research script?",
        "options": [
            "It generates random test problems bounded between a minimum and maximum number of tasks and resources to benchmark algorithm performance",
            "It automatically extracts completed solution source code from web repositories",
            "It computes the line efficiency metrics for an assembly line layout"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 9 - Resource Allocation Optimisation",
        "question": "What happens to the computational performance of an exact MILP solver as resource allocation datasets scale up to very large sizes?",
        "options": [
            "The computation time drops to near zero due to linear relaxation traits",
            "The combinatorial search space expands exponentially, causing the solver to require significant time to prove mathematical optimality",
            "The solver automatically switches to the Hungarian Method to bypass capacity ranges"
        ],
        "correct": 1
    },
    {
        "unit": "Unit 9 - Resource Allocation Optimisation",
        "question": "What is a primary focus of resource allocation optimization in project management contexts?",
        "options": [
            "Allocating skilled staff from different departments to support multiple projects based on priority and availability constraints",
            "Balancing task times evenly across a set of physical workstations along a moving conveyor line",
            "Minimizing sequence-dependent tool setup times on a shared machine asset"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 9 - Resource Allocation Optimisation",
        "question": "What parameter does an optimization model minimize if its objective is focused on workforce scheduling?",
        "options": [
            "The total costs associated with resource deployment, under-utilization, over-time, or skill mismatches",
            "The number of downstream successors linked within a line precedence graph",
            "The total makespan of jobs moving through a sequence of machines"
        ],
        "correct": 0
    },
    {
        "unit": "Unit 9 - Resource Allocation Optimisation",
        "question": "What structural file format must be used to submit your completed homework tasks for evaluation to PoliformaT?",
        "options": [
            "A raw uncompressed folder structure containing Python files",
            "A single ZIP file containing your report template (in both DOCX and PDF formats) alongside your Python source code files",
            "An Excel spreadsheet file containing your raw output matrices"
        ],
        "correct": 1
    }
]

def get_blueprint_exam():
    """
    Pulls exactly 11 questions from Units 1, 2, 3, 4, 6, 7, 8, 9,
    and exactly 12 questions from Unit 5, matching the official 100-question distribution blueprint.
    """
    exam_list = []
    
    # Categorize questions by unit
    by_unit = {}
    for q in RAW_QUESTION_BANK:
        u = q["unit"]
        if u not in by_unit:
            by_unit[u] = []
        by_unit[u].append(q)
        
    # Apply strict selection logic per unit name
    for unit_name, questions in by_unit.items():
        shuffled_pool = list(questions)
        random.shuffle(shuffled_pool)
        
        # Unit 5 gets 12 items, others get 11
        target_count = 12 if "Unit 5" in unit_name else 11
        exam_list.extend(shuffled_pool[:target_count])
        
    return exam_list
