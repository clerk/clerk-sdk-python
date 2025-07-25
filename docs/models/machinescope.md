# MachineScope

Machine scope created successfully for a machine


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `object`                                                     | [models.MachineScopeObject](../models/machinescopeobject.md) | :heavy_check_mark:                                           | N/A                                                          |
| `from_machine_id`                                            | *str*                                                        | :heavy_check_mark:                                           | The ID of the machine that has access to the target machine. |
| `to_machine_id`                                              | *str*                                                        | :heavy_check_mark:                                           | The ID of the machine that is being accessed.                |
| `created_at`                                                 | *int*                                                        | :heavy_check_mark:                                           | Unix timestamp of creation.                                  |