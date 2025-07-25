# MachineScopeDeleted

Machine scope deleted successfully for a machine


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `object`                                                                   | [models.MachineScopeDeletedObject](../models/machinescopedeletedobject.md) | :heavy_check_mark:                                                         | String representing the object's type.                                     |
| `from_machine_id`                                                          | *str*                                                                      | :heavy_check_mark:                                                         | The ID of the machine that had access to the target machine                |
| `to_machine_id`                                                            | *str*                                                                      | :heavy_check_mark:                                                         | The ID of the machine that was being accessed                              |
| `deleted`                                                                  | *bool*                                                                     | :heavy_check_mark:                                                         | Whether the machine scope was successfully deleted                         |